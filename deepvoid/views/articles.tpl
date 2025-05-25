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
                <th>Название</th>
                <th>Автор</th>
                <th>Описание</th>
                <th>Дата</th>
            </tr>
        </thead>
        <tbody id="articles-body">
            % if error:
                <tr><td colspan="4">Ошибка загрузки статей: {{error}}</td></tr>
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