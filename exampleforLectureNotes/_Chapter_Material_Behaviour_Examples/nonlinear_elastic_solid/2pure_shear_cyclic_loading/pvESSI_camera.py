from paraview.simple import *
LoadPlugin("libpvESSI.so",ns=globals());
from paraview.simple import *
# def ResetSession():
#     pxm = servermanager.ProxyManager();
#     pxm.UnRegisterProxies();
#     del pxm;
#     Disconnect();
#     Connect();
# reader = pvESSI(FileName='/home/yuan/Desktop/tttt/DP_1Confine.h5.feioutput');
# reader = pvESSI(FileName='DP_1Confine.h5.feioutput');
import sys
h5fileNAME = sys.argv[1:]

def make_screenshot(h5name, picName):
	#### import the simple module from the paraview
	#### disable automatic camera reset on 'Show'
	paraview.simple._DisableFirstRenderCameraReset()

	# create a new 'pvESSI'
	dP_1Confineh5feioutput = pvESSI(FileName=h5name)

	# get animation scene
	animationScene1 = GetAnimationScene()

	# update animation scene based on data timesteps
	animationScene1.UpdateAnimationUsingDataTimeSteps()

	# get active view
	renderView1 = GetActiveViewOrCreate('RenderView')
	# uncomment following to set a specific view size
	# renderView1.ViewSize = [1073, 836]

	# show data in view
	dP_1Confineh5feioutputDisplay = Show(dP_1Confineh5feioutput, renderView1)
	# trace defaults for the display properties.
	dP_1Confineh5feioutputDisplay.ColorArrayName = [None, '']
	dP_1Confineh5feioutputDisplay.OSPRayScaleArray = 'Boundary_Conditions'
	dP_1Confineh5feioutputDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
	dP_1Confineh5feioutputDisplay.GlyphType = 'Arrow'
	dP_1Confineh5feioutputDisplay.ScalarOpacityUnitDistance = 1.7320508075688772

	# reset view to fit data
	renderView1.ResetCamera()

	# set scalar coloring
	ColorBy(dP_1Confineh5feioutputDisplay, ('POINTS', 'Generalized_Displacements'))

	# rescale color and/or opacity maps used to include current data range
	dP_1Confineh5feioutputDisplay.RescaleTransferFunctionToDataRange(True)

	# show color bar/color legend
	dP_1Confineh5feioutputDisplay.SetScalarBarVisibility(renderView1, True)

	# get color transfer function/color map for 'GeneralizedDisplacements'
	generalizedDisplacementsLUT = GetColorTransferFunction('GeneralizedDisplacements')

	# get opacity transfer function/opacity map for 'GeneralizedDisplacements'
	generalizedDisplacementsPWF = GetOpacityTransferFunction('GeneralizedDisplacements')

	# create a new 'Warp By Vector'
	warpByVector1 = WarpByVector(Input=dP_1Confineh5feioutput)
	warpByVector1.Vectors = ['POINTS', 'Boundary_Conditions']

	# Properties modified on warpByVector1
	warpByVector1.Vectors = ['POINTS', 'Generalized_Displacements']
	warpByVector1.ScaleFactor = 10.0

	# show data in view
	warpByVector1Display = Show(warpByVector1, renderView1)
	# trace defaults for the display properties.
	warpByVector1Display.ColorArrayName = ['POINTS', 'Generalized_Displacements']
	warpByVector1Display.LookupTable = generalizedDisplacementsLUT
	warpByVector1Display.OSPRayScaleArray = 'Boundary_Conditions'
	warpByVector1Display.OSPRayScaleFunction = 'PiecewiseFunction'
	warpByVector1Display.GlyphType = 'Arrow'
	warpByVector1Display.ScalarOpacityUnitDistance = 1.7320508075688772

	# Adjust the scalarbar location
	scalarbar=GetScalarBar(generalizedDisplacementsLUT, renderView1)
	scalarbar.Position=[0.8,0.05]

	# hide data in view
	Hide(dP_1Confineh5feioutput, renderView1)

	# show color bar/color legend
	warpByVector1Display.SetScalarBarVisibility(renderView1, True)

	animationScene1.GoToLast()

	# rescale color and/or opacity maps used to exactly fit the current data range
	warpByVector1Display.RescaleTransferFunctionToDataRange(False)

	# change representation type
	warpByVector1Display.SetRepresentationType('Surface With Edges')

	# set active source
	SetActiveSource(dP_1Confineh5feioutput)

	# show data in view
	dP_1Confineh5feioutputDisplay = Show(dP_1Confineh5feioutput, renderView1)

	# show color bar/color legend
	dP_1Confineh5feioutputDisplay.SetScalarBarVisibility(renderView1, True)

	# hide data in view
	Hide(warpByVector1, renderView1)

	# hide data in view
	Hide(dP_1Confineh5feioutput, renderView1)

	# set active source
	SetActiveSource(warpByVector1)

	# show data in view
	warpByVector1Display = Show(warpByVector1, renderView1)

	# show color bar/color legend
	warpByVector1Display.SetScalarBarVisibility(renderView1, True)

	# reset view to fit data
	renderView1.ResetCamera()

	#change array component used for coloring
	generalizedDisplacementsLUT.RGBPoints = [-0.019999949261546135, 0.231373, 0.298039, 0.752941, -0.009999974630773067, 0.865003, 0.865003, 0.865003, 0.0, 0.705882, 0.0156863, 0.14902]
	generalizedDisplacementsLUT.VectorMode = 'Component'

	# Properties modified on generalizedDisplacementsPWF
	generalizedDisplacementsPWF.Points = [-0.019999949261546135, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

	#change array component used for coloring
	generalizedDisplacementsLUT.VectorComponent = 1

	#change array component used for coloring
	generalizedDisplacementsLUT.VectorComponent = 2

	#change array component used for coloring
	generalizedDisplacementsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.017320464134898777, 0.865003, 0.865003, 0.865003, 0.034640928269797554, 0.705882, 0.0156863, 0.14902]
	generalizedDisplacementsLUT.VectorComponent = 0
	generalizedDisplacementsLUT.VectorMode = 'Magnitude'

	# Properties modified on generalizedDisplacementsPWF
	generalizedDisplacementsPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.034640928269797554, 1.0, 0.5, 0.0]

	#### saving camera placements for all active views

	# current camera placement for renderView1
	renderView1.CameraPosition = [2.0697451238594597, 2.142527588623594, 1.558699401472205]
	renderView1.CameraFocalPoint = [0.4014333799015284, 0.42097521102822894, 0.3676747828186786]
	renderView1.CameraViewUp = [-0.3128165717836196, -0.31643049834666814, 0.8955543155686443]
	renderView1.CameraParallelScale = 0.6928207463044707

	#### uncomment the following to render all views
	view = GetActiveView()
	view.ViewSize = [ 1960, 1024 ]

	RenderAllViews()
	SaveScreenshot(picName)






for eachFile in h5fileNAME:
	picName = str(eachFile).replace("h5.feioutput","jpg")
	make_screenshot(eachFile, picName)


