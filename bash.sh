jobs=()
dir="$(date +%s)_deidara_output"
i=0;

for file in "$@";
do
  if [ ! -f "$file" ]; then
    echo "File $file not found!"
    exit 1
  fi

  jobs[$((2 * i))]="python3 main.py -i $file -o $dir/$file.md -t md"
  jobs[$((((2 * i)) + 1))]="python3 main.py -i $file -o $dir/$file.html -t html"

  i=$((i + 1));
done

mkdir -p "$dir"

parallel --plus ::: "${jobs[@]}"