% rebase('layout.tpl', title=title, year=year)

<div class="jumbotron">
	<h1>Useful articles</h1>
	<p class="lead">
        We are <span class="highlight">DEEPVOID</span>, a company founded in 2007 in St. Petersburg by three girls who turned their time around. We strive for the quality of our equipment to give people the most vivid and loud experiences.
    </p>
    <p>
        At the moment, we are working with various types of lighting and music equipment. Our company also provides the services of DJs, LJs and technicians.
    </p>
</div>

<div class="table-container">
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Author</th>
                <th>Description</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody id="articles-body">
            % if error:
                <tr><td colspan="4">Error uploading articles: {{error}}</td></tr>
            % else:
                % for article in articles:
                    <tr>
                        <td><a href="{{article['link']}}" target="_blank" class="article-link">{{article['title']}}</a></td>
                        <td>{{article['author']}}</td>
                        <td>{{article['description']}}</td>
                        <td>{{article['date']}}</td>
                    </tr>
                % end
            % end
        </tbody>
    </table>
</div>

<div class="article-form">
    <h2>Add a new article</h2>
    % if message:
        <p style="color: white; text-align: center; font-size: 18px">{{message}}</p>
    % end
    <form method="POST" action="/articles">
        <div class="form-row">
            <div class="form-group">
                <label for="title">Title</label>
                <input type="text" id="title" name="title" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="author">Author</label>
                <input type="text" id="author" name="author" class="form-control" required>
            </div>
        </div>
        <div class="form-group">
            <label for="description">Description</label>
            <textarea id="description" name="description" class="form-control" rows="3" required></textarea>
        </div>
        <div class="form-group">
            <label for="link">Link</label>
            <input type="url" id="link" name="link" class="form-control" required>
        </div>
        <button type="submit" class="btn btn-primary">Add article</button>
    </form>
</div>