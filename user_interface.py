import utils
import exoplanets
def main()->None:
    print("This is the astronomy and exoplanets explorer system 🌎🪐 \n")
    path = input("Please write the path of the file\n")
    attributes = exoplanets.data_mapper()
    data = utils.read_data(path, attributes)

    print(data)

main()