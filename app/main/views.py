from app.main.forms import submitblogform, submitcommentform
from flask import render_template,request,redirect,url_for
from . import main
from app.models import Blog, Comment, User 
from flask_login import login_user,login_required,logout_user,current_user
from .. import db, photos

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    user_idd=user.id
    #pitches=Pitch.query.filter_by(user_id=user_idd).all()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)        


@main.route('/user/<uname>/update/pic' , methods=['POST','GET'])
@login_required
def update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])

        path=f'photos/{filename}'
        user.profilepicpath=path

        db.session.commit()
        return redirect(url_for('main.profile',uname=uname))    

@main.route('/submitpitch',methods=['GET','POST'])
@login_required
def submitblog():
    form=submitblogform(request.form)

    id=current_user.id
    
    
    if request.method =='POST' and form.validate_on_submit():
        blog=Blog(title=form.title.data,blog=form.blog.data,user_id=id,name=current_user.username)
        db.session.add(blog)
        db.session.commit()

        
        
        #return redirect(url_for('main.profile',uname=uname))
        
        return redirect(url_for('.blogs'))
                
        #return redirect(url_for('.index'))category
    
    

    #return redirect(url_for('.pitches',category=form.category.data))
    
    return render_template('blog/submitblog.html',form=form,name=current_user.username,user_id=id)


@main.route('/blogs')
def blogs():
    Allblogs=Blog.query.filter().all()

    return render_template('blogs.html',Allblogs=Allblogs)

@main.route('/user/<blogid>/comments',methods=['GET','POST'])
@login_required
def comment(blogid):
    pitch=Blog.query.filter_by(id=blogid).first()
    form=submitcommentform()
    if request.method =='POST' and form.validate_on_submit():
        comment=Comment(comment=form.comment.data,user_id=current_user.id,name=current_user.username,blog_id=blogid)
        db.session.add(comment)
        db.session.commit()

        blogid=blogid
        

        return redirect (url_for('main.singleblog',blogid=blogid))

    return render_template('pitch/comments.html',form=form,blogid=blogid)

@main.route('/<blogid>')
def singleblog(blogid):
    comments=Comment.query.filter_by(blog_id=blogid).all()
    pitch=Blog.query.filter_by(id=blogid).first()
   
    
    return render_template('pitch/singleblog.html',pitch=pitch,comments=comments)
