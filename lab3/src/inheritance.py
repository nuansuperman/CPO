import functools

class loging(object):
  '''
   the class decorator
  '''
  def __init__(self,level="warn"):
    self.level = level
  def __call__(self,func):
    @functools.wraps(func)
    def _deco(*args, **kwargs):
      if self.level == "warn":
        self.notify(func)
      return func(*args, **kwargs)
    return _deco
  def notify(self,func):
    print( "%s is running" % func.__name__)
@loging(level="warn")#执行__call__方法
def bar_A(a,b):
  a=('i am bar:%s'%(a+b))
  return a


class email_loging(loging):
  '''
   Inherit the extended the class decorator
  '''
  def __init__(self, email='1102667245@qq.com', *args, **kwargs):
    self.email = email
    super(email_loging, self).__init__(*args, **kwargs)
  def notify(self,func):
    # 发送一封email到self.email
    print ("%s is running" % func.__name__)
    print("sending email to %s" %self.email)
@email_loging(level="warn")
def bar_B(a,b):
  b=('i am bar:%s'%(a+b))
  return b
