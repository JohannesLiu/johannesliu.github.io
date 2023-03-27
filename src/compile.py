
import os

compile_list = ["index.jemdoc",
                "news.jemdoc",
                "skills.jemdoc",
                "talks.jemdoc",
                "edge-music.jemdoc",
                "papers.jemdoc",
                "opensource-books.jemdoc",
                "opensource-software.jemdoc",
                "opensource-datasets.jemdoc",
                "awards.jemdoc",
                "service.jemdoc",
                "edge-hsc.jemdoc"
                ]

os.system("python jemdoc -c mysite.conf " + " ".join(compile_list))

