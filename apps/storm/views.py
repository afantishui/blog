import markdown
import time
from django.conf import settings
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, BigCategory, Category, Tag
from .models import Article, BigCategory, Category, Tag
from markdown.extensions.toc import TocExtension  # 锚点的拓展
from haystack.generic_views import SearchView  # 导入搜索视图
from haystack.query import SearchQuerySet
# Create your views here.
class IndexView(generic.ListView):
    """
        首页视图,继承自ListVIew，用于展示从数据库中获取的文章列表
    """
    # 获取数据库中的文章列表
    model = Article
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = 'index.html'
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = 'articles'

def AboutView(request):
        return render(request, 'about.html', {'category': 'about'})


class DetailView(generic.DetailView):
    """
        Django有基于类的视图DetailView,用于显示一个对象的详情页，我们继承它
    """
    # 获取数据库中的文章列表
    model = Article

    # template_name属性用于指定使用哪个模板进行渲染
    template_name = 'article.html'

    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = 'article'

    def get_object(self):
        obj = super(DetailView, self).get_object()
        # 设置浏览量增加时间判断,同一篇文章两次浏览超过半小时才重新统计阅览量,作者浏览忽略
        u = self.request.user
        ses = self.request.session
        the_key = 'is_read_{}'.format(obj.id)
        is_read_time = ses.get(the_key)
        if u != obj.author:
            if not is_read_time:
                obj.update_views()
                ses[the_key] = time.time()
            else:
                now_time = time.time()
                t = now_time - is_read_time
                if t > 60 * 30:
                    obj.update_views()
                    ses[the_key] = time.time()
        # 文章可以使用markdown书写，带格式的文章，像csdn写markdown文章一样
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        obj.body = md.convert(obj.body)
        obj.toc = md.toc
        return obj

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['category'] = self.object.id
        return context

# 喜欢点赞
@csrf_exempt
def LoveView(request):
    data_id = request.POST.get('um_id', '')
    if data_id:
        article = Article.objects.get(id=data_id)
        article.loves += 1
        article.save()
        return HttpResponse(article.loves)
    else:
        return HttpResponse('error', status=405)



# 重写搜索视图，可以增加一些额外的参数，且可以重新定义名称
class MySearchView(SearchView):
    # 返回搜索结果集
    context_object_name = 'search_list'
    # 设置分页
    paginate_by = getattr(settings, 'BASE_PAGE_BY', None)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 0)
    # 搜索结果以浏览量排序
    queryset = SearchQuerySet().order_by('-views')