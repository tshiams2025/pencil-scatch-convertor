
import gradio as gr

def get_shipping_quotes(dimensions, weight, destination):
    return f"""
Shipping Quote

Package Dimensions: {dimensions}
Weight: {weight} kg
Destination: {destination}

USPS: $42
UPS: $50
FedEx: $57
"""

app = gr.Interface(
    fn=get_shipping_quotes,
    inputs=[
        gr.Textbox(label="Dimensions (L x W x H)"),
        gr.Number(label="Weight (kg)"),
        gr.Textbox(label="Destination")
    ],
    outputs=gr.Textbox(label="Shipping Quotes"),
    title="Shipping Rate Calculator",
    description="Enter your package information to compare shipping rates."
)

app.launch()