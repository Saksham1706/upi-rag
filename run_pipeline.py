import subprocess
import sys

def run_step(step_name, command):
    print(f"\n{'='*50}")
    print(f"Running step: {step_name}")
    print(f"{'='*50}")

    result = subprocess.run(
        [sys.executable] + command,
        capture_output=False
    )

    if result.returncode != 0:
        print(f"\n❌ Step failed: {step_name}")
        sys.exit(1)

    print(f"✅ Completed: {step_name}")


if __name__ == "__main__":

    run_step(
        "Preprocessing PDFs",
        ["src/preprocess.py"]
    )

    run_step(
        "Creating FAISS embeddings",
        ["src/embed.py"]
    )

    run_step(
        "Saving embeddings",
        ["src/save_embeddings.py"]
    )

    run_step(
        "Running RAG inference",
        ["src/rag.py"]
    )

    print("\n🎉 PIPELINE COMPLETED SUCCESSFULLY")
