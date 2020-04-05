from .auth import *
from .qna import *

urlpatterns = auth.urlpatterns + qna.urlpatterns
