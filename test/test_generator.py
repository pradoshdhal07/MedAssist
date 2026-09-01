from services.generator import Generator


generator = Generator()

query = "What should be done after cleaning the GE MAC 5 device?"

context = """
Document: GE-Resting ECG System (MAC 5) — User & Operation Manual
Page: 272

Cleaning and Disinfection

Inspect the device and trolley to make sure the complete removal
of soil from surfaces, holes, and moveable parts.

If soil is still present, re-clean the equipment by repeating
the cleaning step.

Allow the device to air dry.

Discard wipes to clinical waste.
Do not reuse wipes.
"""

answer = generator.generate(
    query,
    context
)

print("\n===== GEMINI ANSWER =====\n")
print(answer)