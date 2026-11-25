def optimize_prompt(original_prompt, audience, tone, output_format):
    """
    Rule-based prompt optimizer.
    It preserves the user's task but adds role, context, clear instructions,
    structure and quality requirements. It does not call an AI model.
    """
    task = " ".join(original_prompt.split())
    lower_task = task.lower()

    if "artificial intelligence" in lower_task or " ai " in f" {lower_task} ":
        topic_steps = [
            "Define Artificial Intelligence and explain its purpose.",
            "Explain major types or categories of AI.",
            "Describe common real-world applications.",
            "Give at least two practical examples.",
            "Mention important benefits and limitations."
        ]
    elif "machine learning" in lower_task:
        topic_steps = [
            "Define Machine Learning and explain how it works.",
            "Explain supervised, unsupervised and reinforcement learning.",
            "Give practical examples of each relevant type.",
            "Describe common real-world applications.",
            "Mention basic benefits and limitations."
        ]
    elif "python" in lower_task or "programming" in lower_task:
        topic_steps = [
            "Explain the main idea in beginner-friendly language.",
            "Describe the important concepts related to the task.",
            "Give simple, correct code examples where useful.",
            "Explain each example step by step.",
            "Mention practical uses and common mistakes."
        ]
    elif "data science" in lower_task or "data analytics" in lower_task:
        topic_steps = [
            "Explain the meaning and purpose of the topic.",
            "Describe relevant tools, methods and techniques.",
            "Explain the process step by step.",
            "Give practical, real-world examples.",
            "Describe common applications and limitations."
        ]
    else:
        topic_steps = [
            "Begin with a clear definition or introduction.",
            "Break the task into its important parts.",
            "Explain each important point clearly.",
            "Include at least two relevant examples.",
            "End with a concise summary or conclusion."
        ]

    steps = "\n".join(
        f"{number}. {instruction}"
        for number, instruction in enumerate(topic_steps, start=1)
    )

    return f"""ROLE:
Act as a knowledgeable subject expert and a clear teacher.

ORIGINAL TASK TO COMPLETE:
{task}

AUDIENCE:
Write for a {audience.lower()}.

TONE:
Use a {tone.lower()} tone.

REQUIRED OUTPUT FORMAT:
Present the answer as {output_format.lower()}.

IMPROVED TASK INSTRUCTIONS:
{steps}

QUALITY REQUIREMENTS:
1. Make the answer specific to the original task.
2. Explain technical words when needed.
3. Avoid vague, repeated or unrelated information.
4. Use clear headings and a logical order.
5. Check that every part of the original task has been addressed.

FINAL CHECK:
Before giving the answer, make sure it is clear, accurate, complete and suitable for the target audience."""