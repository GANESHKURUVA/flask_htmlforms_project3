from flask import Flask,render_template,request

FAI=Flask(__name__)


@FAI.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        form_name=request.form
        form_pw=request.form
        return form_name,form_pw
    
    return render_template('htmlforms.html')



if __name__=='__main__':
    FAI.run(debug=True)