% rebase('layout.tpl', title=title, year=year)

<div class="body-content container">
    <h1 class="highlight">Orders</h1>

    <form action="/orders" method="post" class="review-form testimonial">
        <div class="form-group" style="margin-bottom: 1rem;">
            <label for="name" class="form-label">Name</label>
            <input id="name" type="text" name="name" value="{{data.get('name', '')}}" class="form-control {{'input-validation-error' if errors.get('name') else ''}}" placeholder="Enter your name">
            % if errors.get('name'):
                <span class="field-validation-error">{{errors['name']}}</span>
            % end
        </div>

        <div class="form-group" style="margin-bottom: 1rem;">
            <label class="form-label">Services</label>
            <div class="services-checkboxes">
                <label class="service-checkbox">
                    <input type="checkbox" name="services" value="sound_equipment" class="service-checkbox-input"
                           {{'checked' if 'sound_equipment' in data.get('services', []) else ''}}>
                    Sound Equipment Rental (15,000 &#8381)
                </label>
                <label class="service-checkbox">
                    <input type="checkbox" name="services" value="light_equipment" class="service-checkbox-input"
                           {{'checked' if 'light_equipment' in data.get('services', []) else ''}}>
                    Light Equipment Rental (10,000 &#8381)
                </label>
                <label class="service-checkbox">
                    <input type="checkbox" name="services" value="stage_structures" class="service-checkbox-input"
                           {{'checked' if 'stage_structures' in data.get('services', []) else ''}}>
                    Stage Structures Rental (20,000 &#8381)
                </label>
                <label class="service-checkbox">
                    <input type="checkbox" name="services" value="special_effects" class="service-checkbox-input"
                           {{'checked' if 'special_effects' in data.get('services', []) else ''}}>
                    Special Effects Equipment Rental (12,000 &#8381)
                </label>
                <label class="service-checkbox">
                    <input type="checkbox" name="services" value="technical_support" class="service-checkbox-input"
                           {{'checked' if 'technical_support' in data.get('services', []) else ''}}>
                    Technical Event Support (25,000 &#8381)
                </label>

            </div>
            % if errors.get('services'):
                <span class="field-validation-error">{{errors['services']}}</span>
            % end
        </div>

        <div class="form-group" style="margin-bottom: 1rem;">
            <label for="description" class="form-label">Description</label>
            <textarea id="description" name="description" rows="5" class="form-control {{'input-validation-error' if errors.get('description') else ''}}">{{data.get('description', '')}}</textarea>
            % if errors.get('description'):
                <span class="field-validation-error">{{errors['description']}}</span>
            % end
        </div>

        <div class="form-group" style="margin-bottom: 1rem;">
            <label for="date" class="form-label">Date (DD.MM.YYYY)</label>
            <input id="date" type="text" name="date" value="{{data.get('date', '')}}" class="form-control {{'input-validation-error' if errors.get('date') else ''}}" placeholder="DD.MM.YYYY">
            % if errors.get('date'):
                <span class="field-validation-error">{{errors['date']}}</span>
            % end
        </div>

        <div class="form-group" style="margin-bottom: 1rem;">
            <label for="phone" class="form-label">Phone (+7(XXX)XXX-XX-XX)</label>
            <input id="phone" type="text" name="phone" value="{{data.get('phone', '')}}" class="form-control {{'input-validation-error' if errors.get('phone') else ''}}" placeholder="+7(XXX)XXX-XX-XX">
            % if errors.get('phone'):
                <span class="field-validation-error">{{errors['phone']}}</span>
            % end
        </div>

        <div class="form-group" style="margin-bottom: 1rem;">
            <label class="form-label">Total Amount</label>
            <span id="total-amount">{{data.get('total_amount', 0)}} &#8381</span>
            <input type="hidden" name="total_amount" id="total-amount-input" value="{{data.get('total_amount', 0)}}">
        </div>

        <button type="submit" class="btn btn-primary w-100">Submit</button>
    </form>

    <hr>

    <h2>Orders List</h2>
    <div class="reviews-list">
        % for order in orders:
            <div class="review-card">
                <div class="review-header">
                    <strong>Order #{{order["order_number"]}} ({{order.get("name", "Unknown")}})</strong>
                </div>
                <p class="review-text"><strong>Services:</strong> {{', '.join([dict(SERVICE_NAMES).get(s, s) for s in order["services"]])}}</p>
                <p class="review-text"><strong>Description:</strong> {{order["description"]}}</p>
                <p class="review-text"><strong>Date:</strong> {{order["date"]}}</p>
                <p class="review-text"><strong>Phone:</strong> {{order["phone"]}}</p>
                <p class="review-text"><strong>Total Amount:</strong> {{order["total_amount"]}} &#8381</p>
                <div class="review-footer">
                    <small>Added: {{order["timestamp"][:19].replace("T", " ")}}</small>
                </div>
            </div>
        % end
    </div>

    <script src="/static/scripts/orders.js"></script>
</div>
