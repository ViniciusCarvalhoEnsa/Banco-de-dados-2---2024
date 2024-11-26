(defun process-element (x)
  (if (>= x 4)
      (* x 2)
      (/ x 2)))

(defun process-list (lst)
  (mapcar 'process-element lst))

(defun combine-lists (lst1 lst2)
  (append (process-list lst1) (process-list lst2)))

(setq result (combine-lists '(1 2 3) '(4 5 6)))
