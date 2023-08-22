from company_info import CompanyInfo
from contact_form import ContactForm

class WebPage:
    def __init__(self):
        self.company_info = CompanyInfo()
        self.contact_form = ContactForm()

    def render(self):
        navbar = self.render_navbar()
        hero_section = self.render_hero_section()
        company_info_section = self.render_company_info()
        services_section = self.render_services()
        reviews_section = self.render_reviews()
        testimonials_section = self.render_testimonials()
        contact_form_section = self.render_contact_form()
        footer_section = self.render_footer()
        portfolio_section = self.render_portfolio()
        
        return f"{navbar}{hero_section}{company_info_section}{services_section}{portfolio_section}{reviews_section}{testimonials_section}{contact_form_section}{footer_section}"

    def render_navbar(self):
        return """<nav class="navbar navbar-expand-lg navbar-custom sticky">
                    <a class="navbar-brand" href="/">Hacktivate Nation</a>
                    <button class="navbar-toggler text-black" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ml-auto">
                            <li class="nav-item">
                                <a class="nav-link" href="/">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/company-info">About</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#contact">Contact</a>
                            </li>
                        </ul>
                    </div>
                   </nav>"""

    def render_hero_section(self):
        return """<section class="hero-section">
                    <div class="container">
                        <div class="row align-items-center">
                        <div class="col-md-6">
                            <h1>Join Hacktivate Nation</h1>
                            <p>We're here to provide you with <strong>top-notch services</strong> for web development, digital marketing, and online education.</p>
                            <a href="/contact" class="btn btn-primary">Get Started</a>
                            <a href="/company-info" class="btn btn-secondary">Learn More</a>
                        </div>
                        
                        </div>
                    </div>
                    </section>
                    """

    def render_services(self):
        return """<section class="py-5">
                    <!-- Create a parent card -->
                    <div class="card">
                    <!-- Add a header for the parent card -->
                    <div class="card-header">
                        <h2>Our Services</h2>
                    </div>
                    <!-- Add a body for the parent card -->
                    <div class="card-body">
                        <!-- Create a row to hold the child cards -->
                        <div class="row">
                        <!-- Create the first child card -->
                        <div class="col-md-4">
                            <div class="card">
                            <div class="card-body">
                                <h3>Online Discord Community</h3>
                                <p>Description: Join our online discord community where you can connect with other coders, share your projects, get feedback, learn new skills, participate in events, and have fun. Whether you are a beginner or an expert, you will find a welcoming and supportive environment where you can grow as a developer.</p>
                            </div>
                            </div>
                        </div>
                        <!-- Create the second child card -->
                        <div class="col-md-4">
                            <div class="card">
                            <div class="card-body">
                                <h3>AI Education Center</h3>
                                <p>Description: Learn about AI from our AI education center, where we offer courses, workshops, webinars, podcasts, and more on various topics related to AI. Whether you want to learn the basics of AI, explore its applications in different domains, or dive into its ethical and social implications, we have something for you.</p>
                            </div>
                            </div>
                        </div>
                        <!-- Create the third child card -->
                        <div class="col-md-4">
                            <div class="card">
                            <div class="card-body">
                                <h3>Web Development Services</h3>
                                <p>Description: Hire us for your web development needs. We are a team of experienced and skilled web developers who can create stunning and responsive websites for your business or personal use. We use the latest technologies and best practices to deliver high-quality results that meet your expectations.</p>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>

                   </section>"""

    def render_testimonials(self):
        return """<section class="py-5 bg-light">
                <h2>What Our Clients Say</h2>
                <div class="row">
                    <div class="col-md-4 my-3">
                        <div class="card review-card">
                            <div class="card-body">
                                <blockquote>
                                    <p>“I learned so much from the AI education center. The courses were engaging and practical, and the instructors were knowledgeable and helpful. I highly recommend it to anyone who wants to learn more about AI.”</p> <footer>— Joe Ramadani, CEO of AI Forecasts</footer> <span>⭐⭐⭐⭐⭐</span>
                                </blockquote>
                            </div>
                        </div>
                    </div>
                        <div class="col-md-4 my-3">
                        <div class="card review-card">
                            <div class="card-body">
                                <blockquote>
                                    <p>“The web development services provided by this company were amazing. They created a stunning and responsive website for my business that exceeded my expectations. They were also very professional, communicative, and timely throughout the whole process. I would highly recommend them to anyone who needs a website.”</p> <footer>— Jane Shannahan, Owner of Jane’s Boutique</footer> <span>⭐⭐⭐⭐⭐</span>
                                </blockquote>
                            </div>
                        </div>
                    </div>
                        <div class="col-md-4 my-3">
                        <div class="card review-card">
                            <div class="card-body">
                                <blockquote>
                                    <p>“This company is more than just a web development service provider. They are also a community of passionate and talented coders who are always willing to help and support each other. I joined their online discord community and I was blown away by the level of engagement, collaboration, and learning that took place there. It was a great experience and I made some new friends along the way.”</p> <footer>— Jose Reynolds, Freelance Web Developer</footer> <span>⭐⭐⭐⭐⭐</span>
                                </blockquote>
                            </div>
                        </div>
                    </div>
                </div>
                   </section>"""

    def render_footer(self):
        return """<footer class="bg-dark text-white py-3 text-center">
                    <p>&copy; 2023 Hacktivate Nation. All rights reserved.</p>
                   </footer>"""

    def render_company_info(self):
        company_name = self.company_info.name
        company_description = self.company_info.description
        return f"""<section class="py-5">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-6">
                                <h1>{company_name}</h1>
                                <p>{company_description}</p>
                                <p>We are a company that believes in the power of coding to create positive change in the world. We are not just a web development service provider, but also an online platform where coders can learn, share, and grow together. Our mission is to create a chill place for people to come and share projects they are working on or find support from a team of individuals all working for a better future.</p>
                            </div>
                            <div class="col-md-6">
                                <img src="/static/company-logo.jpg" alt="Company logo" class="img-fluid">
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-4">
                                <h3>Online Discord Community</h3>
                                    <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
                                        <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
                                    </svg>                                
                                    <ul>
                                    <li>Connect with other coders</li>
                                    <li>Share your projects and get feedback</li>
                                    <li>Learn new skills and participate in events</li>
                                    <li>Have fun in a welcoming and supportive environment</li>
                                </ul>
                            </div>
                            <div class="col-md-4">
                                <h3>AI Education Center</h3>
<svg width="41" height="41" viewBox="0 0 41 41" fill="none" xmlns="http://www.w3.org/2000/svg" stroke-width="1.5" class="h-6 w-6" role="img"><text x="-9999" y="-9999">ChatGPT</text><path d="M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z" fill="currentColor"></path></svg>                                <ul>
                                    <li>Learn about AI from our AI education center</li>
                                    <li>Offer courses, workshops, webinars, podcasts, and more on various topics related to AI</li>
                                    <li>Explore AI applications in different domains</li>
                                    <li>Dive into AI ethical and social implications</li>
                                </ul>
                            </div>
                            <div class="col-md-4">
                                <h3>Web Development Services</h3>
<img alt="icon for web development services from iconscout.com" id="dimg_1" src="data:image/jpeg;base64,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" data-atf="4" data-frt="0">                                <ul>
                                    <li>Hire us for your web development needs</li>
                                    <li>Create stunning and responsive websites for your business or personal use</li>
                                    <li>Use the latest technologies and best practices</li>
                                    <li>Deliver high-quality results that meet your expectations</li>
                                </ul>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-12">
                                <p>We started as a small group of friends who shared a passion for coding and wanted to help each other improve our skills and knowledge. We soon realized that there were many others who shared our vision and values, and we decided to create an online discord community where we could connect with them. From there, we expanded our services to include an AI education center, where we offer courses, workshops, webinars, podcasts, and more on various topics related to AI. We also started offering web development services to clients who needed professional and reliable websites for their businesses or personal use.</p>

                                <p>Today, we are proud to say that we have grown into a large and diverse community of coders who are constantly learning from each other and working on exciting projects that make a difference. We have also received many positive testimonials from our clients who are satisfied with our work and our customer service. We are always looking for new ways to improve our services and our community, and we welcome anyone who wants to join us on our journey.</p>
                            </div>
                        </div>

                    </div>

                </section>"""
    def render_reviews(self):
        reviews = self.company_info.reviews
        reviews_html = ""
        for review in reviews:
            author = review.author
            content = review.content
            review_html = f"""<div class="col-md-4 my-3">
                                <div class="card review-card">
                                    <div class="card-body">
                                        <h3 class="card-title">{author}</h3>
                                        <p class="card-text">{content}</p>
                                    </div>
                                </div>
                            </div>"""
            reviews_html += review_html
        return f"""<section class="py-5">
                    <h2>Reviews</h2>
                    <div class="row">
                        {reviews_html}
                    </div>
                </section>"""



    def render_contact_form(self):
        return f"""<section id="contact" class="py-5">
                    <h2>Contact Us</h2>
                    <div class="contact-form">
                        <form method="POST" action="/submit-contact">
                            <label for="name">Name:</label>
                            <input type="text" id="name" name="name" required>
                            
                            <label for="email">Email:</label>
                            <input type="email" id="email" name="email" required>

                            <label for="subject">Subject:</label>
                            <input type="text" id="subject" name="subject" required>

                            <label for="message">Message:</label>
                            <textarea id="message" name="message" rows="4" required></textarea>
                            
                            <button type="submit">Send Message</button>
                        </form>
                    </div>
                </section>"""

    
    def render_portfolio(self):
        return """<section class="py-5">
                    <h2>Our Projects</h2>
                    <div class="row">
                        <div class="col-md-4 my-3">
                        <div class="card review-card">
                            <img src="/static/project1.jpg" alt="Project 1" class="img-fluid card-img-top">
                            <div class="card-body">
                                <h3>Project 1</h3>
                                <p>Description of Project 1.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 my-3">
                        <div class="card review-card">
                            <img src="/static/project2.jpg" alt="Project 2" class="img-fluid card-img-top">
                            <div class="card-body">
                                <h3>Project 2</h3>
                                <p>Description of Project 2.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4 my-3">
                        <div class="card review-card">
                            <img src="/static/project3.jpg" alt="Project 3" class="img-fluid card-img-top">
                            <div class="card-body">
                                <h3>Project 3</h3>
                                <p>Description of Project 3.</p>
                            </div>
                        </div>
                    </div>
                    </div>
                </section>"""

