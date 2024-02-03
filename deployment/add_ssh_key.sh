set -e

KEY_NAME="Components.pem"
ORIGIN_DIR="$HOME/Downloads"
ORIGIN_KEY="$ORIGIN_DIR/$KEY_NAME"
DEST_DIR="$HOME/.ssh"
DEST_KEY="$DEST_DIR/$KEY_NAME"

mkdir -p "$DEST_DIR"
mv "$ORIGIN_KEY" "$DEST_KEY"
chmod 600 "$DEST_KEY"

eval "$(ssh-agent -s)"
ssh-add "$DEST_KEY"
echo "SSH key '$KEY_NAME' has been setup successfully."
