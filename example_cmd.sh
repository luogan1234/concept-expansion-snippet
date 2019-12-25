zh="data/ZH-"
en="data/EN-"
while getopts "t:" arg
do
  case $arg in
  t)
    case $OPTARG in
    zh0)
      cmd="python main.py -task extract -l zh -it ${zh}DSA-text.txt -is ${zh}DSA-seed.txt -nf"
      echo $cmd
      ;;
    zh1)
      cmd="python main.py -task expand -l zh -it ${zh}DSA-seed.txt -ss baidu -nf"
      echo $cmd
      ;;
    en0)
      cmd="python main.py -task extract -l en -it ${en}DSA-text.txt -is ${en}DSA-seed.txt -nf"
      echo $cmd
      ;;
    en1)
      cmd="python main.py -task expand -l en -is ${en}DSA-seed.txt -ss bing -nf"
      echo $cmd
      ;;
    *)
      echo "unknown value $OPTARG of arg t"
      ;;
    esac
    ;;
  *)
    ;;
  esac
done
$cmd
