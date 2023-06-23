import graphviz
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
from tkinter import messagebox

def render_graph(dot_code, image_format='png', image_file='graph_output'):
    graph = graphviz.Source(dot_code, format=image_format)
    graph.render(filename=image_file, cleanup=True, view=False)
    return f'{image_file}.{image_format}'


def show_dialog():
    message = input_text.get()
    messagebox.showinfo("Dialog Box", f"Entered text: {message}")


def create_tkinter_app():
    root = tk.Tk()
    root.title("Example App")

    # Create a label and text input field
    label = tk.Label(root, text="Enter a string:")
    label.pack()

    input_text = tk.Entry(root)
    input_text.pack()

    # Create a button to show the dialog box
    button = tk.Button(root, text="Show Dialog", command=show_dialog)
    button.pack()

    root.mainloop()


# Example Graphviz DOT code
dot_code = '''
digraph GDPRDataTransferFlow {
    node [shape=box];
    
    subgraph cluster_adequacy_decision {
        label = "Adequacy Decision";
        EU_US_Privacy_Shield [label="EU-US Privacy Shield"];
        EU_US_Privacy_Shield -> Data_Transfer [label="Valid"];
    }
    
    subgraph cluster_scc {
        label = "Standard Contractual Clauses (SCCs)";
        SCCs [label="Standard Contractual Clauses"];
        SCCs -> Data_Transfer [label="Valid"];
    }
    
    subgraph cluster_bcrs {
        label = "Binding Corporate Rules (BCRs)";
        BCRs [label="Binding Corporate Rules"];
        BCRs -> Data_Transfer [label="Valid"];
    }
    
    subgraph cluster_explicit_consent {
        label = "Explicit Consent";
        Consent [label="Explicit Consent"];
        Consent -> Data_Transfer [label="Valid"];
    }
    
    Data_Transfer [label="Data Transfer\n(from Europe to US)"];
    
    EU_US_Privacy_Shield [shape=box];
    SCCs [shape=box];
    BCRs [shape=box];
    Consent [shape=box];
    
    {rank=same; EU_US_Privacy_Shield, SCCs, BCRs, Consent}
}
'''

image_file = render_graph(dot_code)
image_data = Image.open(image_file)

fig, ax = plt.subplots()
ax.imshow(image_data)
plt.axis('off')
plt.show()