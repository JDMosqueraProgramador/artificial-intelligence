// DEGREES TO RECOMMEND:

const degrees = [
  'Ingeniería industrial',
  'Ingeniería de sistemas',
  'Ingeniería civil',
  'Economía',
  'Diseño gráfico',
  'Psicología',
  'Derecho'
];

const questions = {
  'Te gustan las ciencias humanas?': -10,
  'Te gustan la tecnología?': 10,
  'Te gusta tener debates?': -10,
  'Te gustan las matemáticas?': 10,
  'Te gusta el arte?': -10,
  'Te gusta el manejo de herramientas?': 10,
};

const pointsDegree = {
  30: 'Ingeniería industrial',
  20: 'Ingeniería de sistemas',
  10: 'Ingeniería civil',
  0: 'Economía',
  '-10': 'Diseño gráfico',
  '-20': 'Psicología',
  '-30': 'Derecho',
};