import streamlit as st
from prompt_optimizer import optimize_prompt

st.set_page_config(page_title="Smart Prompt Generator", page_icon="✨", layout="wide")

st.title("✨ Smart Prompt Generator & Optimizer")
st.write("Create a new structured prompt or improve an existing one.")

st.info(
    "This version uses Python templates and rules. It creates prompts; "
    "it does not generate the final AI answer or connect to an external AI API."
)
if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []
home_tab, tab1, tab2, history_tab = st.tabs([
    "🏠 Home",
    "🚀 Prompt Generator",
    "⚡ Prompt Optimizer",
    "📚 Prompt History"
])
with home_tab:
    st.divider()

    st.header("📊 Project Statistics")

    history = st.session_state.get("prompt_history", [])

    generated_count = sum(
        1 for item in history if item["type"] == "Generated"
    )

    optimized_count = sum(
        1 for item in history if item["type"] == "Optimized"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Prompts", len(history))
    col2.metric("Generated Prompts", generated_count)
    col3.metric("Optimized Prompts", optimized_count)
    st.title("🏠 Welcome to Smart Prompt Generator")
    st.subheader("Create Better Prompts with Ease")

    st.write(
        "This application helps users create new "
        "prompts and improve existing prompts."
    )

    st.divider()

    st.header("📌 About Our Project")

    st.write(
        "Smart Prompt Generator and Optimizer is a "
        "Python-based application designed to help "
        "users write clear and structured prompts."
    )

    st.write(
        "It provides two main features: "
        "Prompt Generation and Prompt Optimization."
    )

    st.divider()

    st.header("🚀 Our Main Features")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚀 Prompt Generator")
        st.write(
            "Creates a new structured prompt "
            "using the topic and goal entered by the user."
        )

    with col2:
        st.subheader("⚡ Prompt Optimizer")
        st.write(
            "Improves an existing prompt by adding "
            "role, audience, tone and instructions."
        )

    st.divider()

    st.header("📖 How to Use")

    st.markdown("""
    1. Open the Prompt Generator or Prompt Optimizer tab.
    2. Enter your topic or existing prompt.
    3. Select your target audience.
    4. Choose the required tone and output format.
    5. Click the Generate or Optimize button.
    6. Review and download your final prompt.
    """)

    st.divider()

    st.header("💻 Technologies Used")

    st.write("🐍 Python")
    st.write("🌐 Streamlit")
    st.write("🖥️ VS Code")

    st.divider()

    st.info(
        "Note: This project uses Python-based templates "
        "and rules. It does not currently connect to "
        "an external AI API."
    )
with tab1:
    st.subheader("Generate a New Prompt")
    topic = st.text_input("Enter your topic", placeholder="Example: Python programming")
    goal = st.text_area("What do you want to achieve?", placeholder="Example: Learn Python basics with examples")

    audience = st.selectbox(
        "Select your audience",
        ["Beginner", "Student", "Professional", "General Audience"],
        key="gen_audience"
    )
    tone = st.selectbox(
        "Select tone",
        ["Simple", "Professional", "Friendly", "Formal"],
        key="gen_tone"
    )
    output_format = st.selectbox(
        "Select output format",
        ["Paragraph", "Bullet Points", "Step-by-Step", "Table"],
        key="gen_format"
    )

    if st.button("Generate Prompt", key="generate_button", type="primary"):
        if not topic.strip() or not goal.strip():
            st.warning("Please enter both topic and goal.")
        else:
            st.session_state.generated_prompt = f"""ROLE:
Act as an experienced {topic.strip()} teacher and subject expert.

TOPIC:
{topic.strip()}

MAIN GOAL:
{goal.strip()}

AUDIENCE:
Explain this for a {audience.lower()}.

TONE:
Use a {tone.lower()} tone.

RESPONSE STRUCTURE:
Present the answer in {output_format.lower()} format.

DETAILED INSTRUCTIONS:
1. Start with a clear and simple introduction to {topic.strip()}.
2. Explain the key concepts needed to achieve this goal: {goal.strip()}.
3. Include at least two relevant examples.
4. Explain difficult terms in easy language.
5. End with a short summary and useful next steps.

QUALITY RULES:
Keep the answer accurate, relevant, well-organized, and focused on the user's goal."""

            st.session_state.prompt_history.append(dict(
              type="Generated",
              prompt=st.session_state.generated_prompt
            ))
    if "generated_prompt" in st.session_state:
        st.subheader("Generated Prompt")
        st.text_area("Review or edit your generated prompt", value=st.session_state.generated_prompt,
                     height=300, key="generated_output")
        st.write("📋 Copy your generated prompt:")
        st.code(st.session_state.generated_prompt)
        st.download_button("Download Generated Prompt", st.session_state.generated_prompt,
                           file_name="generated_prompt.txt")

with tab2:
    st.subheader("Optimize an Existing Prompt")
    original = st.text_area(
        "Enter your existing prompt",
        height=120,
        placeholder="Example: Explain machine learning."
    )
    opt_audience = st.selectbox(
        "Choose target audience",
        ["Beginner", "Student", "Professional", "General Audience"],
        key="opt_audience"
    )
    opt_tone = st.selectbox(
        "Choose tone",
        ["Simple", "Professional", "Friendly", "Formal"],
        key="opt_tone"
    )
    opt_format = st.selectbox(
        "Choose output format",
        ["Paragraph", "Bullet Points", "Step-by-Step", "Table"],
        key="opt_format"
    )

    if st.button("Optimize Prompt", key="optimize_button", type="primary"):
        if not original.strip():
            st.warning("Please enter a prompt first.")
        else:
            st.session_state.optimized_prompt = optimize_prompt(
                original, opt_audience, opt_tone, opt_format
            )
            st.session_state.prompt_history.append({
                "type": "Optimized",
                "prompt": st.session_state.optimized_prompt
            })

    if "optimized_prompt" in st.session_state:
        st.subheader("Optimized Prompt")
        st.text_area("Review or edit your optimized prompt",
                     value=st.session_state.optimized_prompt,
                     height=330, key="optimized_output")
        st.write("📋 Copy your optimized prompt:")
        st.code(st.session_state.optimized_prompt)
        st.download_button("Download Optimized Prompt", st.session_state.optimized_prompt,
                           file_name="optimized_prompt.txt")
with history_tab:
    st.subheader("📚 Your Prompt History")

    if st.session_state.prompt_history:
        for i, item in enumerate(reversed(st.session_state.prompt_history), 1):
            with st.expander(f"{i}. {item['type']} Prompt"):
                st.code(item["prompt"])
                st.download_button(
                    "Download Prompt",
                    item["prompt"],
                    file_name=f"history_prompt_{i}.txt",
                    key=f"history_download_{i}"
                )

        if st.button("Clear History"):
            st.session_state.prompt_history = []
            st.rerun()

    else:
        st.info("No prompt history available. Generate or optimize a prompt first.")
st.divider()
st.caption("Smart Prompt Generator & Optimizer | Python + Streamlit")

