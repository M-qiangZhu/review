backends = {'simple': True}


def Graph(backend=None):
    if not backend: backend = 'simple'
    print(backend)
    if backend:
        return "hhaha"


print(Graph())