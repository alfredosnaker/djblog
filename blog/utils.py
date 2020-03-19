from docx  import Document


def modify_document(file_=None, text_to_replace={}):
    
    
    if not file_:
        return 'No se encontro ningun archivo'
    try:    
        f = open(file_, 'rb')
    except Exception as e:
        return e
    document = Document(f)
    f.close()
    #document_copy = document
    for paragraph in document.paragraphs:
        for keyword, new_text in text_to_replace.items():
            if keyword in paragraph.text:
                inline = paragraph.runs
                for i in range(len(inline)):
                    if keyword in inline[i].text:
                        text = inline[i].text.replace(keyword, new_text)
                        inline[i].text = text
    
    name = 'new_document.docx'
    #path_new_document = f'/temporal/{name}'
    document.save(name)

    return document


    def savedocument(self):
        path_to_file = '/home/alfredo/Escritorio/lorem_ipsum(copia).docx'
        text_to_replace = {
            'believable': 'believable Changed',
            'Lorem': 'Lorem Changed',
            'structures': 'SUSTITUIBLE NOW!'
        }
        doc = modify_document(file=path_to_file, text_to_replace=text_to_replace)