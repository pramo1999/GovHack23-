#!/bin/bash
# mkdir temp/6_clean
# for filename in temp/1998/6/*.jpg; do
#     echo $filename
#     # echo $(basename "$filename")
#     # echo convert $filename temp/5_clean/$(basename "$filename")
#     # convert 115.pdf-1.jpg -set page -%[fx:w*0.12]-%[fx:h*0.12] -crop 66%x+0+0 res.jpg
#     echo convert $filename -set page -%[fx:w*0.12]-%[fx:h*0.12] -crop 66%x+0+0 temp/6_clean/$(basename "$filename")
#     convert $filename -set page -%[fx:w*0.12]-%[fx:h*0.12] -crop 66%x+0+0 temp/6_clean/$(basename "$filename")
# done

# #!/bin/bash
# for filename in temp/5_clean/*.jpg; do
#     echo $filename
#     # echo $(basename "$filename")
#     # echo convert $filename temp/5_clean/$(basename "$filename")
#     # convert 115.pdf-1.jpg -set page -%[fx:w*0.12]-%[fx:h*0.12] -crop 66%x+0+0 res.jpg
#     # echo convert $filename -resize 40% temp/5_clean_small/$(basename "$filename").png
#     convert $filename -resize 40% temp/5_clean_small/$(basename "$filename").png
# done

# mkdir temp/6_clean_gray
# for filename in temp/6_clean/*.jpg; do
#     echo $filename
#     convert $filename -set colorspace Gray -separate -average -auto-gamma -contrast temp/6_clean_gray/$(basename "$filename")
# done

# mkdir temp/5_clean_gray
# for filename in temp/5_clean/*.jpg; do
#     echo $filename
#     convert $filename -set colorspace Gray -separate -average temp/5_clean_gray/$(basename "$filename")
# done

mkdir temp/7_clean
for filename in temp/1998/7/*.jpg; do
    echo $filename
    # echo $(basename "$filename")
    # echo convert $filename temp/5_clean/$(basename "$filename")
    # convert 115.pdf-1.jpg -set page -%[fx:w*0.12]-%[fx:h*0.12] -crop 66%x+0+0 res.jpg
    echo convert $filename -set page -%[fx:w*0.12]-%[fx:h*0.12] -crop 66%x+0+0 temp/7_clean/$(basename "$filename")
    convert $filename -set page -%[fx:w*0.12]-%[fx:h*0.12] -crop 66%x+0+0 temp/7_clean/$(basename "$filename")
done