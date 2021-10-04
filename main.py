from lib.parser import LaGouParser

if __name__ == '__main__':
    lg = LaGouParser()
    lg.cookie = ''
    lg.course_ids = ''
    lg.save_path='./lg'
    lg.download_article = True
    lg.article2md = True
    lg.article2pdf = True
    lg.download_video = True
    lg.use_parallel = True
    lg.run()
