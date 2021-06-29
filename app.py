import streamlit as st

st.sidebar.markdown('### Настройки')
languages = ['rus', 'eng']
selected_languages = st.sidebar.selectbox('Язык', languages)

st.markdown('### 1 Загрузите файл')
upload_file_object = st.file_uploader('', ['pdf', 'png', 'jpg'])
if not upload_file_object:
    st.stop()

# кэширование файла
filename = upload_file_object.name
if not upload_file_object.closed:
    print(f'Dumping file to cache {filename}...')
    with open(filename, 'wb') as outfile:
        outfile.write(upload_file_object.getvalue())

st.markdown('### 2 Результат преобразования')

# pdf to image
text_representation = ''
if filename.endswith('pdf'):
    text_representation = 'pdf file'
else:
    text_representation = '123' # image to text

st.text(text_representation)
st.stop()
