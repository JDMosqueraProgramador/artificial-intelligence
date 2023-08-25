;;; SE para ayudar en la decisión de una carrera UNIVERSITARIA
;;;
;;;

(defrule startDegreeRecommender
=> 
  (printout t "Hola, el sistema te realizará algunas preguntas con el fin de indetificar la mejor carrera universitaria para tí" crlf)
  (printout t "Ingrese 1 para decir Sí, 0 para decir No " crlf)

  (printout t "¿Te gustan las ciencias humanas?" crlf)
  (bind ?humanScience (read))
  (assert (humanScience ?humanScience))

  (printout t "¿Te gustan la tecnología?" crlf)
  (bind ?tecnology (read))
  (assert (tecnology ?tecnology))

  (printout t "¿Te gusta tener debates?" crlf)
  (bind ?discuss (read))
  (assert (discuss ?discuss))

  (printout t "¿Te gustan las matemáticas?" crlf)
  (bind ?mathemathics (read))
  (assert (mathemathics ?mathemathics))

  (printout t "¿Te gusta el arte?" crlf)
  (bind ?art (read))
  (assert (art ?art))

  (printout t "¿Te gusta el manejo de herramientas?" crlf)
  (bind ?tools (read))
  (assert (tools ?tools))
)

(deffunction calculateProfile
  (?humanScienceValue ?tecnologyValue ?discussValue ?mathemathicsValue ?artValue ?toolsValue)
  (+ ?humanScienceValue ?tecnologyValue ?discussValue ?mathemathicsValue ?artValue ?toolsValue)
)

(defrule assignValueToHumanScience
  (humanScience ?humanScience)
  => 
  (if (eq ?humanScience 1) then
    (bind ?humanScienceValue -10)
    else (bind ?humanScienceValue 0)
  )
  (assert (humanScienceValue ?humanScienceValue))
)

(defrule assignValueToTecnology
  (tecnology ?tecnology)
  => 
  (if (eq ?tecnology 1) then
    (bind ?tecnologyValue 10)
    else (bind ?tecnologyValue 0)
  )
  (assert (tecnologyValue ?tecnologyValue))
)

(defrule assignValueToDiscuss
  (discuss ?discuss)
  => 
  (if (eq ?discuss 1) then
    (bind ?discussValue -10)
    else (bind ?discussValue 0)
  )
  (assert (discussValue ?discussValue))
)

(defrule assignValueToMathemathics
  (mathemathics ?mathemathics)
  => 
  (if (eq ?mathemathics 1) then
    (bind ?mathemathicsValue 10)
    else (bind ?mathemathicsValue 0)
  )
  (assert (mathemathicsValue ?mathemathicsValue))
)

(defrule assignValueToArt
  (art ?art)
  => 
  (if (eq ?art 1) then
    (bind ?artValue -10)
    else (bind ?artValue 0)
  )
  (assert (artValue ?artValue))
)

(defrule assignValueToTools
  (tools ?tools)
  => 
  (if (eq ?tools 1) then
    (bind ?toolsValue 10)
    else (bind ?toolsValue 0)
  )
  (assert (toolsValue ?toolsValue))
)

(defrule calculateProfileValue
  (humanScienceValue ?humanScienceValue) 
  (tecnologyValue ?tecnologyValue) 
  (discussValue ?discussValue) 
  (mathemathicsValue ?mathemathicsValue) 
  (artValue ?artValue) 
  (toolsValue ?toolsValue)
  =>
  (bind ?caculatedDegree (calculateProfile ?humanScienceValue ?tecnologyValue ?discussValue ?mathemathicsValue ?artValue ?toolsValue) )
  (assert (caculatedDegree ?caculatedDegree))
)

(defrule recommendDegree
  (caculatedDegree ?caculatedDegree)
  => 
  (if (eq ?caculatedDegree -30) then (bind ?degree "Derecho"))
  (if (eq ?caculatedDegree -20) then (bind ?degree "Psicología"))
  (if (eq ?caculatedDegree -10) then (bind ?degree "Diseño gráfico"))
  (if (eq ?caculatedDegree 0) then (bind ?degree "Economía"))
  (if (eq ?caculatedDegree 10) then (bind ?degree "Ingeniería civil"))
  (if (eq ?caculatedDegree 20) then (bind ?degree  "Ingeniería de sistemas"))
  (if (eq ?caculatedDegree 30) then (bind ?degree "Ingeniería industrial"))

  (printout t "Tu carrera recomendada es: " ?degree crlf)
)