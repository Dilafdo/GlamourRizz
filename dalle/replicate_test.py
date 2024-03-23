import replicate

output = replicate.run(
    "lucataco/dreamshaper-xl-turbo:0a1710e0187b01a255302738ca0158ff02a22f4638679533e111082f9dd1b615",
    input={
        "width": 1024,
        "height": 1024,
        "prompt": "photo of a Cat poised gracefully atop an ancient oak tree, autumn leaves fluttering around, golden hour casting long shadows, backlit, sharp focus on feline, bokeh effect on background foliage, digital painting.",
        "scheduler": "K_EULER",
        "num_outputs": 1,
        "guidance_scale": 2,
        "apply_watermark": True,
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast",
        "num_inference_steps": 6
    }
)
print(output)