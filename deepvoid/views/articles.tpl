% rebase('layout.tpl', title=title, year=year)

<!-- Секция с заголовком и описанием компании -->
<div class="jumbotron">
	<h1>Useful articles</h1>
	<p class="lead">
        We are <span class="highlight">DEEPVOID</span>, a company founded in 2007 in St. Petersburg by three girls who turned their time around. We strive for the quality of our equipment to give people the most vivid and loud experiences.
    </p>
    <p>
        At the moment, we are working with various types of lighting and music equipment. Our company also provides the services of DJs, LJs and technicians.
    </p>
</div>

<!-- Контейнер для таблицы со списком статей -->
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
            <!-- Если ошибка есть, показываем её -->
            % if error:
                <tr><td colspan="4">Error uploading articles: {{error}}</td></tr>
            % else:
                % for article in articles:
                    <tr>
                        <td><a href="{{article['link']}}" target="_blank" class="article-link">{{article['title']}}</a></td> <!-- Название статьи как ссылка -->
                        <td>{{article['author']}}</td>
                        <td>{{article['description']}}</td>
                        <td>{{article['date']}}</td>
                    </tr>
                % end
            % end
        </tbody>
    </table>
</div>

<!-- Форма для добавления новой статьи -->
<div class="article-form">
    <h2>Add a new article</h2>
    % if 'general' in form_errors:
        <div class="field-validation-error">{{form_errors['general']}}</div>
    % end
    <form method="POST" action="/articles"> <!-- Форма отправляет данные методом POST на /articles -->
        <div class="form-row">
            <div class="form-group">
                <!-- Название -->
                <label for="title">Title</label>
                <input type="text" id="title" name="title" class="form-control" required value="{{form_data.get('title','')}}">
                % if 'title' in form_errors:
                    <span class="field-validation-error" style="color: #ff00dc">{{form_errors['title']}}</span>
                % end
            </div>
            <div class="form-group">
                <!-- Автор -->
                <label for="author">Author</label>
                <input type="text" id="author" name="author" class="form-control" required value="{{form_data.get('author','')}}">
                % if 'author' in form_errors:
                    <span class="field-validation-error" style="color: #ff00dc">{{form_errors['author']}}</span>
                % end
            </div>
        </div>
        <div class="form-group">
            <!-- Описание -->
            <label for="description">Description</label>
            <textarea id="description" name="description" class="form-control" rows="3" required>{{!form_data.get('description','')}}</textarea>
            % if 'description' in form_errors:
                <span class="field-validation-error" style="color: #ff00dc">{{form_errors['description']}}</span>
            % end
        </div>
        <div class="form-group">
            <!-- Ссылка -->
            <label for="link">Link</label>
            <input type="url" id="link" name="link" class="form-control" required value="{{form_data.get('link','')}}">
        </div>
        <button type="submit" class="btn btn-primary">Add article</button>
    </form>
</div>