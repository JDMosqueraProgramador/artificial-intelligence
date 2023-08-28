;;; SE para ayudar en la elección de una carrera UNIVERSITARIA
;;;
;;;

(defrule startDegreeRecommender
=> 
  (printout t "Hola, el sistema te realizará algunas preguntas con el fin de indetificar la mejor carrera universitaria para tí" crlf)
  (printout t "Ingrese 1 para decir Sí, 0 para decir No " crlf)

 (printout t "¿Te gustan las ciencias humanas?" crlf)
  (bind ?humanScience (read))
  (assert (humanScience ?humanScience))


 (printout t "¿Te sientes satisfecho cuando puedes ayudar a encontrar una solución justa para diferentes partes involucradas?" crlf)
  (bind ?conflictResolution (read))
  (assert (conflictResolution ?conflictResolution))

  (printout t "¿Te gustan la tecnología?" crlf)
  (bind ?tecnology (read))
  (assert (tecnology ?tecnology))

  (printout t "¿Te gusta trabajar en proyectos creativos y artísticos?" crlf)
  (bind ?creativity (read))
  (assert (creativity ?creativity))

  (printout t "¿Te gusta tener debates?" crlf)
  (bind ?discuss (read))
  (assert (discuss ?discuss))

  (printout t "¿Tienes un fuerte interés por saber cómo funcionan los sistemas y las máquinas?" crlf)
  (bind ?interestSystems (read))
  (assert (interestSystems ?interestSystems))

  (printout t "¿Te gustan las matemáticas?" crlf)
  (bind ?mathemathics (read))
  (assert (mathemathics ?mathemathics))

  (printout t "¿Te encuentras a menudo brindando apoyo emocional y consejos a amigos y familiares?" crlf)
  (bind ?empathy (read))
  (assert (empathy ?empathy))

  (printout t "¿Te gusta el arte?" crlf)
  (bind ?art (read))
  (assert (art ?art))


  (printout t "¿Disfrutas resolver rompecabezas, acertijos y problemas que requieren un pensamiento lógico y estructurado?" crlf)
  (bind ?logicReasoning (read))
  (assert (logicReasoning ?logicReasoning))

  (printout t "¿Te gusta el manejo de herramientas?" crlf)
  (bind ?tools (read))
  (assert (tools ?tools))
  
  (printout t "¿Te atrae la idea de diseñar y planificar sistemas, procesos y flujos de trabajo?" crlf)
  (bind ?planning (read))
  (assert (planning ?planning))
)

(deffunction calculateProfile
  (?humanScienceValue ?tecnologyValue ?discussValue ?mathemathicsValue ?artValue ?toolsValue
?conflictResolutionValue ?empathyValue ?interestSystemsValue ?creativityValue ?logicReasoningValue ?planningValue)
  (+ ?humanScienceValue ?tecnologyValue ?discussValue ?mathemathicsValue ?artValue ?toolsValue
?conflictResolutionValue ?empathyValue ?interestSystemsValue ?creativityValue ?logicReasoningValue ?planningValue)
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


(defrule assignValueToempathy
  (empathy ?empathy)
  => 
  (if (eq ?empathy 1) then
    (bind ?empathyValue -5)
    else (bind ?empathyValue 0)
  )
  (assert (empathyValue ?empathyValue))
)


(defrule assignValueToconflictResolution
  (conflictResolution ?conflictResolution)
  => 
  (if (eq ?conflictResolution 1) then
    (bind ?conflictResolutionValue -5)
    else (bind ?conflictResolutionValue 0)
  )
  (assert (conflictResolutionValue ?conflictResolutionValue))
)



(defrule assignValueTointerestSystems
  (interestSystems ?interestSystems)
  => 
  (if (eq ?interestSystems 1) then
    (bind ?interestSystemsValue 5)
    else (bind ?interestSystemsValue 0)
  )
  (assert (interestSystemsValue ?interestSystemsValue))
)

(defrule assignValueTocreativity
  (creativity ?creativity)
  => 
  (if (eq ?creativity 1) then
    (bind ?creativityValue -5)
    else (bind ?creativityValue 0)
  )
  (assert (creativityValue ?creativityValue))
)

(defrule assignValueTologicReasoning
  (logicReasoning ?logicReasoning)
  => 
  (if (eq ?logicReasoning 1) then
    (bind ?logicReasoningValue 5)
    else (bind ?logicReasoningValue 0)
  )
  (assert (logicReasoningValue ?logicReasoningValue))
)

(defrule assignValueToplanning
  (planning ?planning)
  => 
  (if (eq ?planning 1) then
    (bind ?planningValue 5)
    else (bind ?planningValue 0)
  )
  (assert (planningValue ?planningValue))
)




(defrule calculateProfileValue
  (humanScienceValue ?humanScienceValue) 
  (tecnologyValue ?tecnologyValue) 
  (discussValue ?discussValue) 
  (mathemathicsValue ?mathemathicsValue) 
  (artValue ?artValue) 
  (toolsValue ?toolsValue)
  (empathyValue ?empathyValue)
  (conflictResolutionValue ?conflictResolutionValue)
  (interestSystemsValue ?interestSystemsValue)
  (creativityValue ?creativityValue)
  (logicReasoningValue ?logicReasoningValue)
  (planningValue ?planningValue)
  =>
  (bind ?caculatedDegree (calculateProfile ?humanScienceValue ?tecnologyValue ?discussValue ?mathemathicsValue ?artValue ?toolsValue
   ?empathyValue ?conflictResolutionValue ?interestSystemsValue ?creativityValue ?logicReasoningValue ?planningValue) )
  (assert (caculatedDegree ?caculatedDegree))
)

(defrule recommendDegree
  (caculatedDegree ?caculatedDegree)
  => 
  (if (or (= ?caculatedDegree -30) (= ?caculatedDegree -25)) then (bind ?degree "Derecho"))
  (if (or (= ?caculatedDegree -20) (= ?caculatedDegree -15)) then (bind ?degree "Psicología"))
  (if (or (= ?caculatedDegree -10) (= ?caculatedDegree -5)) then (bind ?degree "Diseño gráfico"))
  (if (eq ?caculatedDegree 0) then (bind ?degree "Economía"))
  (if (or (= ?caculatedDegree 5) (= ?caculatedDegree 10)) then (bind ?degree "Ingeniería civil"))
  (if (or (= ?caculatedDegree 15) (= ?caculatedDegree 20)) then (bind ?degree  "Ingeniería de sistemas"))
  (if (or (= ?caculatedDegree 25) (= ?caculatedDegree 30)) then (bind ?degree "Ingeniería industrial"))

  (printout t "Tu carrera recomendada es: " ?degree crlf)
)
