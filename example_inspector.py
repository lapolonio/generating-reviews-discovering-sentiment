from encoder import Model
from generate_html import generate_sentiment_html

positive_sample = """
Just what I was looking for. Nice fitted pants, exactly
matched seam to color contrast with other pants I own.
Highly recommended and also very happy!"""

negative_sample = """
They didn’t fit either. Straight high sticks at the end. On
par with other buds I have. Lesson learned to avoid.
"""

complete_sample = """
This is one of Crichton’s best books. The characters of Karen Ross, Peter Elliot, Munro, and Amy are beautifully developed and their interactions are exciting, complex, and fast-paced throughout this impressive novel. And about 99.8 percent of that got lost in the film. Seriously, the screenplay AND the directing were horrendous and clearly done by people who could not fathom what was good about the novel. I can’t fault the actors because frankly, they never had a chance to make this turkey live up to Crichton’s original work.  I know good novels, especially those with a science fiction edge, are hard to bring to the screen in a way that lives up to the original. But this may be the absolute worst disparity in quality between novel and screen adaptation ever. The book is really, really good. The movie is just dreadful.
"""


def generate_strings(sample):
    return [sample[1:x] for x in range(1, len(sample))]


def generate_fine_grain_neuron_example(sample, html_name):
    model = Model()
    iterative_strings = generate_strings(sample)
    sample_features = model.transform(iterative_strings)
    generate_sentiment_html(sample_features[:, 2388], sample, html_name)


generate_fine_grain_neuron_example(positive_sample, "positive.html")
generate_fine_grain_neuron_example(negative_sample, "negative.html")
generate_fine_grain_neuron_example(complete_sample, "complete.html")