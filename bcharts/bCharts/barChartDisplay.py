# -------------------------------------------------------------------------------
# Generated by PixieDust code generator
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Inherited from maven-artifact https://github.com/hamnis/maven-artifact
# -------------------------------------------------------------------------------

from pixiedust.display.chart.renderers import PixiedustRenderer
from .rendererBaseDisplay import BChartsBaseDisplay
from pixiedust.utils import Logger
import bchartsclient

@PixiedustRenderer(id="barChart")
@Logger()
class BChartsbarChartDisplay(BChartsBaseDisplay):

    """
        Last validation before rendering:
        Return tuple (True|False, "error message")
    """
    def canRenderChart(self):
        return super(BChartsbarChartDisplay, self).canRenderChart()
        keyFields = self.getKeyFields()

    """
        Main rendering method
    """
    def doRenderChart(self):
        #get the working Pandas Data Frame generated from user selections
        df = self.getWorkingPandasDataFrame()

        #get the key Fields selected by user
        keyFields = self.getKeyFields()

        #get Value Fields selected by user
        valueFields = self.getValueFields()

        client = bchartsclient.Client("", "")

        chart = client.create(df.to_csv(index = False), "discreteBar")

        h = self.getPreferredOutputHeight()
        w = self.getPreferredOutputWidth()
        
        sharelink = self.options.get("chartURL") == 'true'

        # if (self.options.get("showDesigner", "No") == "Yes"):
        if (self.options["showDesigner"] == "Yes"):
            return chart.render()._repr_html_(h=h, w=w, sharelink=sharelink) + chart.render_designer()._repr_html_(h=h, w=w, sharelink=sharelink)

        return chart.render()._repr_html_(h=h, w=w, sharelink=sharelink)

    def getChartContext(self, handlerId):
        diagTemplate = BChartsBaseDisplay.__module__ + ":bChartsOptionsDialogBody.html"
        return (diagTemplate, {})



