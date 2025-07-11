from pipeline.extract import extract_from_excel
from pipeline.transform import contact_data_frames
from pipeline.load import load_excel

if __name__ == '__main__':
    listas_data_frame = extract_from_excel("data/input")
    print(type(listas_data_frame))
    data_frame = contact_data_frames(listas_data_frame)
    print(type(data_frame))
    load_excel(data_frame, "data/output", "output")
    print()


listas_data_frame = extract_from_excel("data/input")

print(listas_data_frame)