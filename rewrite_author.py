def commit_callback(commit):
    if commit.author_email == b'13039207+liumaomaoa@user.noreply.gitee.com':
        commit.author_email = b'Lila.6s.Leslie@gmail.com'
        commit.author_name = '刘黎'
    if commit.committer_email == b'13039207+liumaomaoa@user.noreply.gitee.com':
        commit.committer_email = b'Lila.6s.Leslie@gmail.com'
        commit.committer_name = '刘黎'
