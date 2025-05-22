% rebase('layout.tpl', title=title, year=year)

<div class="body-content container">
    <h1 class="highlight">Reviews</h1>

    <form action="/reviews" method="post" class="review-form testimonial">
        <div class="form-group" style="margin-bottom: 1rem;">
    <label for="author" class="form-label">Username</label>
    <input id="author" type="text" name="author" value="{{data['author']}}"
           class="form-control {{'input-validation-error' if errors.get('author') else ''}}">
    % if errors.get('author'):
        <span class="field-validation-error">{{errors['author']}}</span>
    % end
</div>

    <!-- NEW: Phone input -->
    <div class="form-group" style="margin-bottom: 1rem;">
        <label for="phone" class="form-label">Phone Number</label>
        <input id="phone" type="text" name="phone" value="{{data.get('phone', '')}}"
               class="form-control {{'input-validation-error' if errors.get('phone') else ''}}">
        % if errors.get('phone'):
            <span class="field-validation-error">{{errors['phone']}}</span>
        % end
    </div>

        <div class="form-group" style="margin-bottom: 1rem;">
            <label for="text" class="form-label">Review</label>
            <textarea id="text" name="text" rows="5"
                      class="form-control {{'input-validation-error' if errors.get('text') else ''}}">{{data['text']}}</textarea>
            % if errors.get('text'):
                <span class="field-validation-error">{{errors['text']}}</span>
            % end
        </div>

        <button type="submit" class="btn btn-primary w-100">Submit</button>
    </form>

    <hr>

    <h2>Reviews List</h2>
    <div class="reviews-list">
        % for review in reviews:
            <div class="review-card">
                <div class="review-header">
                    <strong>{{review["author"]}}</strong>
                </div>
                <p class="review-text">{{review["text"]}}</p>
                <div class="review-footer">
                    <small>Added: {{review["timestamp"][:19].replace("T", " ")}}</small>
                </div>
            </div>
        % end
    </div>
</div>
