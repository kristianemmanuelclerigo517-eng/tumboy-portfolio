
import streamlit as st
from pathlib import Path

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Menchy M. Tumboy | Portfolio",
    page_icon="🌿",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600;700&display=swap');

.stApp {
    background: #f5f1e8;
    color: #34463b;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background: #354c3d;
    border-right: 1px solid #627b65;
}

[data-testid="stSidebar"] * {
    color: #f5f1e8 !important;
}

h1, h2, h3 {
    font-family: 'DM Serif Display', serif !important;
    color: #49634e !important;
}

p, li, label {
    color: #455448;
}

.hero {
    background: #354c3d;
    border-radius: 22px;
    padding: 48px;
    margin-bottom: 28px;
    border-bottom: 6px solid #c78b68;
}

.hero-tag {
    color: #d9b18f;
    letter-spacing: 4px;
    font-size: 11px;
    font-weight: 700;
}

.hero-name {
    font-family: 'DM Serif Display', serif;
    font-size: 48px;
    color: #fff8ed;
    line-height: 1.15;
    margin-top: 18px;
}

.hero-desc {
    color: #e4e8dc;
    font-size: 14px;
    line-height: 1.9;
    max-width: 680px;
    margin-top: 20px;
}

.panel {
    background: #fffdf7;
    border: 1px solid #dedbca;
    border-radius: 17px;
    padding: 25px;
    margin-bottom: 18px;
}

.panel-tag {
    color: #b77a59;
    letter-spacing: 3px;
    font-size: 10px;
    font-weight: 700;
}

.panel-title {
    font-family: 'DM Serif Display', serif;
    color: #49634e;
    font-size: 25px;
    margin-top: 8px;
    margin-bottom: 12px;
}

.accent {
    color: #b77a59;
    font-weight: 700;
}

.quote {
    background: #e7eadc;
    border-left: 5px solid #b77a59;
    padding: 22px;
    border-radius: 8px;
    color: #49634e;
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
}

.stButton > button {
    background: #49634e;
    color: white;
    border: none;
    border-radius: 8px;
}

.stButton > button:hover {
    background: #66816a;
    color: white;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# ---------------- IMAGE FUNCTION ----------------
def show_image(filename, caption=None):
    image_path = IMAGE_DIR / filename

    if image_path.is_file():
        st.image(
            str(image_path),
            caption=caption,
            use_container_width=True
        )
    else:
        st.info(f"Add {filename} to your images folder to display it.")


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("# MENCHY.")
    st.caption("A PERSONAL JOURNAL")
    st.markdown("---")

    page = st.radio(
        "EXPLORE MY WORLD",
        [
            "Home",
            "About Me",
            "Education",
            "Movies",
            "Cooking",
            "Music",
            "Adventure",
            "Mechanical Engineering"
        ]
    )

    st.markdown("---")
    st.caption("LITTLE MOMENTS. BIG EXPERIENCES.")


# ---------------- HOME PAGE ----------------
if page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">WELCOME TO MY LITTLE CORNER</div>
        <div class="hero-name">
            MENCHY M.<br>TUMBOY
        </div>
        <p class="hero-desc">
            A collection of my interests, experiences, and dreams.
            From enjoying a good movie and preparing something delicious
            to discovering new places and appreciating music, this space
            reflects the simple things that make life interesting.
        </p>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.3, 1])

    with left:
        st.markdown("## Life Is Made of Little Adventures")

        st.write("""
        I believe that life becomes more meaningful when we make time
        for the things that bring us happiness and allow us to discover
        something new. Sometimes, that means enjoying a movie after
        a long day, experimenting with a recipe in the kitchen,
        listening to music that matches my mood, or stepping outside
        to experience a new adventure.

        These interests may seem simple, but each one gives me a
        different way to relax, express myself, and appreciate the
        experiences that life has to offer.

        Alongside these personal interests, I am also pursuing
        Mechanical Engineering, where I continue to explore the
        technical side of the world and learn how ideas can become
        practical solutions.
        """)

        st.markdown("""
        <div class="quote">
            "Collect moments, discover possibilities, and never stop growing."
        </div>
        """, unsafe_allow_html=True)

    with right:
        show_image("profile.jpg", "Menchy M. Tumboy")


# ---------------- ABOUT ME ----------------
elif page == "About Me":

    st.markdown("# GETTING TO KNOW ME")
    st.caption("A LITTLE INTRODUCTION TO MY PERSONAL WORLD")

    st.markdown("""
    <div class="panel">
        <div class="panel-tag">MY STORY</div>
        <div class="panel-title">Finding Joy in Different Experiences</div>

        My name is <span class="accent">Menchy M. Tumboy</span>.
        I enjoy exploring different activities that make my everyday
        life more interesting and memorable. Whether I am watching
        a movie, trying something in the kitchen, listening to my
        favorite music, or going on an adventure, I appreciate
        experiences that allow me to enjoy the present moment.

        I believe that having different interests gives us more
        opportunities to learn about ourselves and see the world
        from different perspectives. Each hobby has its own charm,
        and together they represent the different things I enjoy
        outside my academic responsibilities.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Four Things That Make My Days Interesting")

    col1, col2 = st.columns(2)

    with col1:
        show_image("movies.jpg", "Stories on screen")

        st.markdown("""
        <div class="panel">
            <div class="panel-tag">01 / ENTERTAINMENT</div>
            <div class="panel-title">Watching Movies</div>
            I enjoy watching movies because they allow me to experience
            different stories, characters, and emotions. Every film
            introduces a new perspective, whether through exciting
            adventures, meaningful lessons, or unforgettable moments.
        </div>
        """, unsafe_allow_html=True)

        show_image("cooking.jpg", "Creative moments in the kitchen")

        st.markdown("""
        <div class="panel">
            <div class="panel-tag">02 / CREATIVITY</div>
            <div class="panel-title">Cooking</div>
            Cooking is an enjoyable way to explore creativity through
            food. I like the idea of combining ingredients, discovering
            flavors, and turning simple preparations into something
            satisfying. It is also a reminder that meaningful results
            often come from patience and effort.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        show_image("music.jpg", "Music for every mood")

        st.markdown("""
        <div class="panel">
            <div class="panel-tag">03 / EXPRESSION</div>
            <div class="panel-title">Listening to Music</div>
            Music is something I can enjoy in almost any situation.
            It can make an ordinary day feel lighter, help me relax,
            or provide the perfect background for different moments.
            I appreciate how different songs can express feelings
            that are sometimes difficult to put into words.
        </div>
        """, unsafe_allow_html=True)

        show_image("adventure.jpg", "Discovering new experiences")

        st.markdown("""
        <div class="panel">
            <div class="panel-tag">04 / EXPLORATION</div>
            <div class="panel-title">Adventure</div>
            I enjoy the excitement of experiencing something new.
            Adventures give me opportunities to discover unfamiliar
            places, appreciate different surroundings, and create
            memories outside my usual routine. Every experience
            brings a chance to learn and see life differently.
        </div>
        """, unsafe_allow_html=True)


# ---------------- EDUCATION ----------------
elif page == "Education":

    st.markdown("# MY EDUCATIONAL JOURNEY")
    st.caption("EVERY EXPERIENCE IS PART OF THE STORY")

    st.markdown("""
    <div class="panel">
        <div class="panel-tag">SENIOR HIGH SCHOOL</div>
        <div class="panel-title">Pamaypayan Integrated School</div>

        My senior high school experience at Pamaypayan Integrated
        School became an important part of my academic and personal
        development. It gave me opportunities to gain knowledge,
        build relationships, strengthen my abilities, and experience
        the responsibilities that come with being a student.

        The lessons and experiences from this stage helped prepare
        me for the challenges and opportunities of college life.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
        <div class="panel-tag">COLLEGE EDUCATION</div>
        <div class="panel-title">North Eastern Mindanao State University</div>

        <b>Program: Bachelor of Science in Mechanical Engineering</b>

        Continuing my education at North Eastern Mindanao State
        University marks another important step in my journey.
        As a Mechanical Engineering student, I am learning about
        the relationship between mathematics, science, design,
        and the mechanical systems that help make modern technology
        possible.

        College challenges me to become more analytical,
        responsible, and determined. It also gives me opportunities
        to develop the knowledge and skills that I can eventually
        apply in real-world engineering situations.
    </div>
    """, unsafe_allow_html=True)


# ---------------- MOVIES ----------------
elif page == "Movies":

    st.markdown("# MOVIE MOMENTS")
    st.caption("A GOOD STORY CAN TAKE YOU SOMEWHERE ELSE")

    left, right = st.columns([1, 1])

    with left:
        show_image("movies.jpg", "The magic of storytelling")

    with right:
        st.markdown("""
        <div class="panel">
            <div class="panel-tag">MY FIRST HOBBY</div>
            <div class="panel-title">A World Beyond the Screen</div>

            Watching movies is one of the ways I enjoy my free time.
            I appreciate how films combine storytelling, visuals,
            music, and performances to create experiences that can
            make people laugh, feel inspired, or think deeply.

            Each movie has something different to offer. Some introduce
            exciting worlds and unexpected adventures, while others
            focus on emotions, relationships, and meaningful life
            lessons. I enjoy discovering these stories and appreciating
            the creativity behind every film.
        </div>
        """, unsafe_allow_html=True)


# ---------------- COOKING ----------------
elif page == "Cooking":

    st.markdown("# MY LITTLE KITCHEN")
    st.caption("CREATIVITY SERVED ONE DISH AT A TIME")

    left, right = st.columns([1, 1])

    with left:
        show_image("cooking.jpg", "Creating something delicious")

    with right:
        st.markdown("""
        <div class="panel">
            <div class="panel-tag">MY SECOND HOBBY</div>
            <div class="panel-title">The Joy of Cooking</div>

            Cooking is a hobby that allows me to enjoy the process
            of creating something with my own hands. From preparing
            ingredients to combining different flavors, every step
            offers an opportunity to experiment and learn.

            What makes cooking interesting is that even simple
            ingredients can become something special when combined
            with creativity and care. It is an enjoyable activity
            that teaches patience while giving me the satisfaction
            of seeing the results of my effort.
        </div>
        """, unsafe_allow_html=True)


# ---------------- MUSIC ----------------
elif page == "Music":

    st.markdown("# MUSIC AND MOOD")
    st.caption("EVERY SONG HAS ITS OWN FEELING")

    left, right = st.columns([1, 1])

    with left:
        show_image("music.jpg", "A soundtrack for everyday life")

    with right:
        st.markdown("""
        <div class="panel">
            <div class="panel-tag">MY THIRD HOBBY</div>
            <div class="panel-title">Listening Beyond the Melody</div>

            Listening to music is one of my favorite ways to relax
            and enjoy my time. I like how songs can match different
            moods and how a particular melody can make an ordinary
            moment feel more memorable.

            Music can provide comfort during quiet moments,
            energy when I need motivation, and enjoyment whenever
            I simply want to appreciate a good song. It is a small
            part of my daily life that brings its own kind of happiness.
        </div>
        """, unsafe_allow_html=True)


# ---------------- ADVENTURE ----------------
elif page == "Adventure":

    st.markdown("# THE SPIRIT OF ADVENTURE")
    st.caption("NEW PLACES, NEW EXPERIENCES, NEW MEMORIES")

    left, right = st.columns([1, 1])

    with left:
        show_image("adventure.jpg", "Every journey begins somewhere")

    with right:
        st.markdown("""
        <div class="panel">
            <div class="panel-tag">MY FOURTH HOBBY</div>
            <div class="panel-title">Beyond the Usual Routine</div>

            Adventure is about giving myself the chance to experience
            something different. I enjoy the thought of exploring
            new surroundings, seeing unfamiliar places, and making
            memories through experiences outside my everyday routine.

            Every adventure offers something to discover. It can
            be a beautiful destination, an unexpected experience,
            or simply a moment that becomes special because of
            the people and places involved. For me, these experiences
            make life more exciting and remind me that there is
            always something new waiting to be explored.
        </div>
        """, unsafe_allow_html=True)


# ---------------- MECHANICAL ENGINEERING ----------------
elif page == "Mechanical Engineering":

    st.markdown("# MECHANICAL ENGINEERING")
    st.caption("TURNING KNOWLEDGE AND CREATIVITY INTO PRACTICAL SOLUTIONS")

    st.markdown("""
    <div class="panel">
        <div class="panel-tag">MY COLLEGE PROGRAM</div>
        <div class="panel-title">Bachelor of Science in Mechanical Engineering</div>

        Mechanical Engineering is a field that brings together
        mathematics, physics, creativity, and technology to understand,
        design, develop, and improve machines and mechanical systems.

        As a student at North Eastern Mindanao State University,
        I am given the opportunity to explore the principles that
        explain how machines function and how different components
        work together. The course introduces important areas such
        as engineering design, mechanics, thermodynamics, and
        other concepts that contribute to the development of
        useful technologies.

        This journey requires patience, critical thinking,
        discipline, and the willingness to learn from challenges.
        It encourages me to look beyond the surface of things
        and understand the science and processes behind them.

        My goal is to continue developing my technical knowledge,
        strengthen my problem-solving abilities, and prepare
        myself for a future where I can contribute to meaningful
        engineering projects and innovations.
    </div>
    """, unsafe_allow_html=True)

    show_image("engineering.jpg", "Discovering the world of engineering")


# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:25px;">
    <p style="color:#49634e; font-family:'DM Serif Display'; font-size:23px;">
        MENCHY M. TUMBOY
    </p>
    <p style="color:#9b8c78; font-size:11px; letter-spacing:2px;">
        A PERSONAL JOURNAL · BUILT WITH STREAMLIT
    </p>
</div>
""", unsafe_allow_html=True)
