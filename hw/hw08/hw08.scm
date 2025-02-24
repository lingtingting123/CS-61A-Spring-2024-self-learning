(define (ascending? s) 
    (   if (or (null? s) (= (length s) 1))
            #t
            (and (or (< (car s) (car (cdr s))) (= (car s) (car (cdr s)))) 
                (ascending? (cdr s))
            )
    )
)

(define (my-filter pred s) 
    (if (null? s)
        nil
        (if (pred (car s))
            (append (list (car s)) (my-filter pred (cdr s)))
            (my-filter pred (cdr s))
        )
    )
)

(define (interleave lst1 lst2) 
    (cond 
        ((and (null? lst1) (null? lst2)) nil)
        ((and (null? lst1) (not (null? lst2))) lst2)
        ((and (not (null? lst1)) (null? lst2)) lst1)
        (else (append (list (car lst1)) (list (car lst2)) (interleave (cdr lst1) (cdr lst2))))
    )
)

(define (no-repeats s) 
    (if (null? s)
        nil
        (if (= (length s) 1)
            s
            (append (list(car s)) (filter (lambda (elem) (not (= (car s) elem))) (no-repeats (cdr s))))
        )
    )
)
