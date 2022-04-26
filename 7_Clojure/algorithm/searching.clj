(ns searching)

(defn search? [numlist target]
    "search function"
    (.indexOf numlist target))

(defn bsearch? [numlist target]
    "binary search function"
    (def uppercount (dec (count numlist)))
    (loop [lower 0
           upper uppercount]
        (if (> lower upper) -1
            (let [mid (quot (+ lower upper) 2)
                  midvalue (nth numlist mid)]
                (cond
                    (> midvalue target) (recur lower (dec mid))
                    (< midvalue target) (recur (inc mid) upper)
                    (= midvalue target) mid)))))
