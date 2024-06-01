from huggingface_hub import HfApi
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("model_path", type=str)
parser.add_argument("repo_id", type=str)
parser.add_argument("-c", "--commit_message", type=str)
args = parser.parse_args()

api = HfApi()

if not api.repo_exists(repo_id=args.repo_id):
    print(f"Creating repo {args.repo_id}")
    api.create_repo(repo_id=args.repo_id, private=True)

print(f"Uploading model from {args.model_path} to {args.repo_id}")
api.upload_folder(
    folder_path=args.model_path,
    repo_id=args.repo_id,
    repo_type="model",
    commit_message=args.commit_message,
    ignore_patterns=["checkpoint-*"],
)

print(f"Uploading checkpoint from {args.model_path} to {args.repo_id}")
api.upload_folder(
    folder_path=args.model_path,
    repo_id=args.repo_id,
    repo_type="model",
    commit_message="Upload checkpoint",
    allow_patterns=["checkpoint-*"],
    create_pr=True
)
