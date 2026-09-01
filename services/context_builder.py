class ContextBuilder:

    def build(self, results):
        context = []

        for result in results:
            chunk = result["chunk"]

            context.append(
                f"Document: {chunk.document_name}\n"
                f"Page: {chunk.page_number}\n"
                f"Text:\n{chunk.text}"
            )

        return "\n\n---\n\n".join(context)