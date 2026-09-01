from services.retriever import Retriever
from services.context_builder import ContextBuilder
from services.generator import Generator


def main():

    print("=" * 60)
    print("                 MEDASSIST")
    print("      Medical Document Question Answering")
    print("=" * 60)

    # ----------------------------------------
    # Initialize components
    # ----------------------------------------

    print("\nLoading MedAssist...")

    retriever = Retriever(
        index_path="./index/medassist.faiss",
        chunks_path="./index/chunks.pkl"
    )

    builder = ContextBuilder()
    generator = Generator()

    print("MedAssist loaded successfully.")
    print("\nType 'exit' to quit.")

    # ----------------------------------------
    # Question-answer loop
    # ----------------------------------------

    while True:

        query = input("\nEnter your question: ").strip()

        if query.lower() == "exit":
            print("\nExiting MedAssist. Goodbye!")
            break

        if not query:
            print("Please enter a question.")
            continue

        try:

            # 1. Retrieve relevant chunks
            results = retriever.retrieve(
                query,
                top_k=7
            )

            if not results:
                print("\nNo relevant information found.")
                continue

            # 2. Build context from retrieved chunks
            context = builder.build(results)

            # 3. Generate answer using Gemini
            answer = generator.generate(
                query,
                context
            )

            # 4. Display answer
            print("\n" + "=" * 60)
            print("                    ANSWER")
            print("=" * 60)
            print(answer)

            # ----------------------------------------
            # 5. Display sources
            # ----------------------------------------

            print("\n" + "-" * 60)
            print("                    SOURCES")
            print("-" * 60)

            seen_sources = set()

            for result in results:

                chunk = result["chunk"]

                source = (
                    chunk.document_name,
                    chunk.page_number
                )

                # Avoid displaying the same document/page multiple times
                if source in seen_sources:
                    continue

                print(
                    f"- {chunk.document_name} — "
                    f"Page {chunk.page_number}"
                )

                seen_sources.add(source)

        except Exception as e:

            print("\nSomething went wrong:")
            print(e)


if __name__ == "__main__":
    main()