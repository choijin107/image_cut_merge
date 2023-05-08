import cut_image
import merge_image
import merge_image_template


if __name__ == '__main__':

    #cut_image.main("lena.png", 5, 4, "lena_cut")
    merge_image.main("lena_cut", 5, 4, "lena_merge.png")
    #merge_image_template.main("lena_cut", 5, 4, "lena_merge.png")