from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def landing_page():
    # Placeholder data for the landing page
    company_name = "Vizyx"
    hero_title = "Empowering Businesses with AI and Data-Driven Solutions"
    hero_description = "At Vizyx, our mission is to empower businesses with the transformative potential of AI and data-driven solutions. We simplify complex processes, optimize decision-making, and unlock new insights that drive operational efficiency and competitive advantage. Through cutting-edge tools and personalized support, we help our clients realize the full value of their data, enabling them to make smarter, faster decisions that fuel growth and innovation."
    
    services = [
        {
            "title": "Data Analytics",
            "description": "Unlock the power of your data with our advanced analytics solutions.",
            "image_placeholder": "data-analytics.png"
        },
        {
            "title": "Machine Learning",
            "description": "Leverage AI to predict trends and make data-driven decisions.",
            "image_placeholder": "deep-learning.png"
        },
        {
            "title": "Data Visualization",
            "description": "Transform complex data into clear, actionable insights.",
            "image_placeholder": "data-visualization.png"
        }
    ]
    
    testimonials = [
        {
            "quote": "DataTech Solutions revolutionized our approach to data!",
            "author": "Jane Doe, CEO of TechCorp"
        },
        {
            "quote": "Their insights helped us increase revenue by 30%.",
            "author": "John Smith, CTO of InnovateCo"
        }
    ]
    
    # Add animated background
    animated_background = url_for('static', filename='animated_background.gif')
    
    # Add demo video placeholder
    demo_video = url_for('static', filename='meta_demo_raw.mp4')
    
    return render_template('landing_page.html',
                           company_name=company_name,
                           hero_title=hero_title,
                           hero_description=hero_description,
                           services=services,
                           testimonials=testimonials,
                           animated_background=animated_background,
                           demo_video=demo_video)

if __name__ == '__main__':
    app.run(debug=True)
