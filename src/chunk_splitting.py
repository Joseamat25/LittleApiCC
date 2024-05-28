from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_chunk(chunk):
    splitter = RecursiveCharacterTextSplitter(
                                              chunk_size=512,
                                              chunk_overlap=75,
                                              )
    return splitter.split_text(chunk)


if __name__ == "__main__":
    example = """
Napoleón Bonaparte (nacido Napoleone Buonaparte; Ajaccio, 15 de agosto de 1769-Santa Elena, 5 de mayo de 1821) más tarde conocido por su nombre regio Napoleón I, fue un militar y político francés de origen italiano nacido en Córcega que saltó a la fama durante la Revolución francesa y dirigió exitosas campañas durante las Guerras revolucionarias. Fue el líder de facto de la República Francesa como primer cónsul desde 1799 hasta 1804, y después emperador de los franceses desde 1804 hasta 1814 y de nuevo en 1815. El legado político y cultural de Napoleón perdura hasta nuestros días, como líder tan célebre como controvertido. Inició muchas reformas liberales que han perdurado en la sociedad, y se le considera uno de los más grandes comandantes militares de la historia. Sus campañas aún se estudian en las academias militares de todo el mundo. Entre tres y seis millones de civiles y soldados murieron en lo que se conoció como las guerras napoleónicas.4​5​

Napoleón nació en la isla de Córcega, poco después de su anexión por Francia, en el seno de una familia nativa descendiente de la pequeña nobleza italiana.6​7​ Apoyó la Revolución francesa en 1789 mientras servía en el ejército francés, e intentó difundir sus ideales en su Córcega natal. Ascendió rápidamente en el ejército tras salvar al Directorio francés en el poder disparando contra insurgentes monárquicos. En 1796, inició una campaña militar contra los austriacos y sus aliados italianos, anotándose victorias decisivas y convirtiéndose en un héroe nacional. Dos años más tarde, dirigió una expedición militar a Egipto que le sirvió de trampolín hacia el poder político. Organizó un golpe de Estado en noviembre de 1799 y se convirtió en primer cónsul de la República."""
    output = split_chunk(example)
    print(output)