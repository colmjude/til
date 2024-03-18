#! /usr/bin/env sh
set -e

if [ -f ./.env ]; then
  export $(cat .env | xargs)
fi

FILE=$1
DEST=$2

echo $FILE

# scp -P $WEBPORT -r $(find $FILE -type f -not -name '.DS_Store') $WEBHOST:$PATHTODIR/$DEST
scp -P $WEBPORT -r $FILE $WEBHOST:$PATHTODIR/$DEST
