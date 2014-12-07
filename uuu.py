def washingmachine(weight_machine, washround, nextround):
    jeans_dark, top_dark, sktr_dark = input(), input(), input()
    jeans_light, top_light, sktr_light = input(), input(), input()
    dark = (jeans_dark*550)+(top_dark*200)+(sktr_dark*300)
    light = (jeans_light*550)+(top_light*200)+(sktr_light*300)
    if dark > 0 and light > 0:
        while dark > weight_machine:
            washround += 1
            dark -= weight_machine
        while dark > (weight_machine/2):
            washround += 1
            dark -= weight_machine
        if dark > 0:
            nextround += 1
        print washround, nextround
        washround = 0
        nextround = 0
        while light > weight_machine:
            washround += 1
            light -= weight_machine
        while light > (weight_machine/2):
            washround += 1
            light -= weight_machine
        if light > 0:
            nextround += 1
        print washround, nextround
    elif dark > 0 or light == 0:
        while dark > (weight_machine/2):
            washround += 1
            dark -= weight_machine
        if dark > 0:
            nextround += 1
        print washround, nextround
    elif light > 0 or dark == 0:
        while light > weight_machine:
            washround += 1
            light -= weight_machine
        while light > (weight_machine/2):
            washround += 1
            light -= weight_machine
        if light > 0:
            nextround += 1
        print washround, nextround
washingmachine(input()*1000, 0, 0)
