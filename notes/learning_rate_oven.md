
# Learning Rate — Explained Like Adjusting Oven Temperature

The learning rate controls how big each update step is during training.  
It determines how fast or slow the model learns.

A good analogy is adjusting the temperature on an oven.

---

## 1. The Oven Analogy

You’re trying to bake something at the perfect temperature.

- If you turn the oven up **way too high**, the food burns.
- If you set it **too low**, nothing cooks.
- If you adjust the temperature carefully, the food cooks perfectly.

The learning rate works exactly like this.

---

## 2. Too High = Overshooting

If the learning rate is too high:

- The model takes huge steps.
- It “overshoots” the best solution.
- The error jumps all over the place.
- Training fails.

Just like cranking the oven to 500°F ruins the dish.

---

## 3. Too Low = Slow Learning

If the learning rate is too low:

- The model takes tiny steps.
- It moves very slowly toward the solution.
- Training can take forever.

This is like trying to bake at 100°F — nothing happens.

---

## 4. Just Right = Efficient Learning

A good learning rate:

- Takes steps that are not too big or too small.
- Reduces error steadily.
- Converges to the best solution efficiently.

Just like cooking at the correct temperature gives you the perfect result.

---

## 5. Summary

The learning rate is:

- The “temperature setting” of your model.
- Too high → unstable.
- Too low → slow.
- Just right → efficient learning.
