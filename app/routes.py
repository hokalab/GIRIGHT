from flask import Blueprint, request, render_template, redirect, url_for
from .forms import GearForm
from .models import Gear
from . import db
from collections import defaultdict

main = Blueprint('main', __name__)

@main.route('/')
def index():
    gears = Gear.query.all()
    return render_template('index.html', gears=gears)

@main.route('/add', methods=['GET', 'POST'])
def add_gear():
    # フォーム初期化のとき GETパラメータから値を拾うようにする
    if request.method == 'GET':
        form = GearForm(data=request.args)
    else:
        form = GearForm()

    if form.validate_on_submit():
        # 重複チェック
        existing = Gear.query.filter_by(
            name=form.name.data,
            manufacturer=form.manufacturer.data,
            category=form.category.data
        ).first()

        if existing and request.args.get('confirm') != 'true':
            # 確認画面を表示（confirm引数がないときだけ）
            return render_template('add_gear_confirm.html', form=form, existing=existing)

        gear = Gear(
            name=form.name.data,
            manufacturer=form.manufacturer.data,
            weight=form.weight.data,
            category=form.category.data,
            essential=form.essential.data,
            is_packed=form.is_packed.data,
            notes=form.notes.data
        )
        db.session.add(gear)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('add_gear.html', form=form)

@main.route('/stats')
def stats():
    from sqlalchemy import func
    category_weights = db.session.query(
        Gear.category,
        func.sum(Gear.weight)
    ).group_by(Gear.category).all()

    labels = [cat.capitalize() for cat, _ in category_weights]
    data = [weight for _, weight in category_weights]

    return render_template('stats.html', labels=labels, data=data)

@main.route('/edit/<int:gear_id>', methods=['GET', 'POST'])
def edit_gear(gear_id):
    gear = Gear.query.get_or_404(gear_id)
    form = GearForm(obj=gear)
    if form.validate_on_submit():
        form.populate_obj(gear)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_gear.html', form=form, gear=gear)

@main.route('/delete/<int:gear_id>', methods=['POST'])
def delete_gear(gear_id):
    gear = Gear.query.get_or_404(gear_id)
    db.session.delete(gear)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/toggle_pack/<int:gear_id>', methods=['POST'])
def toggle_pack(gear_id):
    gear = Gear.query.get_or_404(gear_id)
    gear.is_packed = not gear.is_packed
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/packlist')
def packlist():
    packed_gears = Gear.query.filter_by(is_packed=True).all()
    total_weight = sum([g.weight for g in packed_gears])
    target_weight = 5000
    over = total_weight - target_weight

    category_weights = defaultdict(float)
    for gear in packed_gears:
        category_weights[gear.category] += gear.weight

    return render_template(
        'packlist.html',
        gears=packed_gears,
        total_weight=total_weight,
        target_weight=target_weight,
        over=over,
        category_weights=dict(category_weights)
    )

@main.route('/search')
def search_gear():
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    results = Gear.query
    if query:
        results = results.filter(Gear.name.ilike(f'%{query}%'))
    if category:
        results = results.filter(Gear.category == category)
    results = results.all()
    
    # 検索結果のキーを作成
    search_result_keys = {f"{g.name}|{g.manufacturer}|{g.category}" for g in results}
    
    # 登録済み全ギアからキーを作成
    existing_gears = db.session.query(Gear.name, Gear.manufacturer, Gear.category).all()
    existing_keys = {f"{name}|{manufacturer}|{category}" for name, manufacturer, category in existing_gears}
    
    # 検索結果と重複しないものだけ残す（重複フラグ用）
    external_keys = existing_keys - search_result_keys
    
    return render_template(
        'search_results.html',
        results=results,
        query=query,
        selected_category=category,
        existing_keys=external_keys
    )

@main.route('/quick_add', methods=['POST'])
def quick_add():
    gear = Gear(
        name=request.form.get('name'),
        manufacturer=request.form.get('manufacturer'),
        weight=request.form.get('weight'),
        category=request.form.get('category'),
        essential=False,
        is_packed=False,
        notes=request.form.get('notes')
    )
    db.session.add(gear)
    db.session.commit()
    return redirect(url_for('main.index'))