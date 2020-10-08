<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="1" maxScale="0" readOnly="0" simplifyDrawingHints="1" simplifyAlgorithm="0" simplifyMaxScale="1" minScale="100000000" simplifyDrawingTol="1" version="3.14.1-Pi" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal endField="" accumulate="0" mode="0" startExpression="" fixedDuration="0" startField="" durationField="" endExpression="" enabled="0" durationUnit="min">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 symbollevels="1" attr="TRIM(IF(&quot;S20AH&quot; IS NULL, &quot;VM_STATUS&quot;, CONCAT(&quot;VM_STATUS&quot;,&quot;S20AH&quot;)))&#xa;" forceraster="0" type="categorizedSymbol" enableorderby="0">
    <categories>
      <category value="rem_end" symbol="0" render="true" label="Category A or B area containing endangered"/>
      <category value="rem_oc" symbol="1" render="true" label="Category A or B area containing of concern"/>
      <category value="rem_leastc" symbol="2" render="true" label="Category A or B area that is least concern"/>
      <category value="rem_endVMA S20AH area" symbol="3" render="true" label="Category A or B area containing endangered and is S20AH"/>
      <category value="rem_ocVMA S20AH area" symbol="4" render="true" label="Category A or B area containing of concern and is S20AH"/>
      <category value="rem_leastcVMA S20AH area" symbol="5" render="true" label="Category A or B area that is least concern and is S20AH"/>
      <category value="hvr_end" symbol="6" render="true" label="Category C or R area containing endangered"/>
      <category value="hvr_oc" symbol="7" render="true" label="Category C or R area containing of concern"/>
      <category value="hvr_leastc" symbol="8" render="true" label="Category C or R area that is of least concern"/>
      <category value="water VMA S20AH area" symbol="9" render="true" label="Water (S20AH)"/>
      <category value="water" symbol="10" render="true" label="Water"/>
      <category value="non_remnant" symbol="11" render="true" label="Category X area"/>
      <category value="" symbol="12" render="false" label="Not defined or map rendering error"/>
    </categories>
    <symbols>
      <symbol name="0" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,54,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="101,101,101,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="1" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,101,15,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="101,101,101,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="10" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="225,255,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="11" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="254,255,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="2,2,2,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="12" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="ShapeburstFill" enabled="1" locked="0" pass="0">
          <prop v="0" k="blur_radius"/>
          <prop v="50,6,54,255" k="color"/>
          <prop v="0,0,255,255" k="color1"/>
          <prop v="0,255,0,255" k="color2"/>
          <prop v="0" k="color_type"/>
          <prop v="0" k="discrete"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_map_unit_scale"/>
          <prop v="MM" k="distance_unit"/>
          <prop v="255,255,255,255" k="gradient_color2"/>
          <prop v="0" k="ignore_rings"/>
          <prop v="5" k="max_distance"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="gradient" k="rampType"/>
          <prop v="1" k="use_whole_shape"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="2" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="125,255,177,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="101,101,101,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="3" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,54,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,255,115,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1.7" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="4" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,101,15,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,255,115,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1.7" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="5" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="125,255,177,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="255,255,115,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1.7" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="6" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,168,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="168,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="7" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,208,145,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="168,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="8" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="215,255,177,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="168,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="1" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="9" clip_to_extent="1" alpha="1" type="fill" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="225,255,255,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="Point" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontUnderline="0" fontStrikeout="0" fontLetterSpacing="0" allowHtml="0" fontItalic="0" textColor="0,0,0,255" useSubstitutions="0" fontSize="6" textOpacity="1" fontWordSpacing="0" fontCapitals="0" fontSizeUnit="Point" blendMode="0" fontWeight="50" fieldName="CONCAT(&quot;RE&quot;, '\n', &quot;PC_LABEL&quot; )" textOrientation="horizontal" multilineHeight="1" previewBkgrdColor="255,255,255,255" isExpression="1" namedStyle="Normal" fontFamily="Sans Serif" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontKerning="1">
        <text-buffer bufferSizeUnits="MM" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferOpacity="1" bufferNoFill="1" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferBlendMode="0" bufferSize="0.7" bufferDraw="1"/>
        <text-mask maskSize="0" maskOpacity="1" maskType="0" maskJoinStyle="128" maskedSymbolLayers="" maskEnabled="0" maskSizeUnits="MM" maskSizeMapUnitScale="3x:0,0,0,0,0,0"/>
        <background shapeSVGFile="" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeSizeType="0" shapeJoinStyle="64" shapeSizeUnit="MM" shapeBorderWidthUnit="MM" shapeOpacity="1" shapeDraw="0" shapeSizeY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeBorderColor="128,128,128,255" shapeBlendMode="0" shapeOffsetX="0" shapeOffsetY="0" shapeRadiiUnit="MM" shapeOffsetUnit="MM" shapeRotationType="0" shapeSizeX="0" shapeRadiiY="0" shapeRadiiX="0" shapeRotation="0" shapeBorderWidth="0">
          <symbol name="markerSymbol" clip_to_extent="1" alpha="1" type="marker" force_rhr="0">
            <layer class="SimpleMarker" enabled="1" locked="0" pass="0">
              <prop v="0" k="angle"/>
              <prop v="145,82,45,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowOffsetUnit="MM" shadowColor="0,0,0,255" shadowDraw="0" shadowOffsetAngle="135" shadowScale="100" shadowOffsetDist="1" shadowBlendMode="6" shadowUnder="0" shadowRadiusAlphaOnly="0" shadowRadius="1.5" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOpacity="0.7" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetGlobal="1" shadowRadiusUnit="MM"/>
        <dd_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format addDirectionSymbol="0" autoWrapLength="0" formatNumbers="0" reverseDirectionSymbol="0" leftDirectionSymbol="&lt;" placeDirectionSymbol="0" decimals="3" wrapChar="" useMaxLineLengthForAutoWrap="1" rightDirectionSymbol=">" multilineAlign="1" plussign="0"/>
      <placement rotationAngle="0" placementFlags="10" preserveRotation="1" layerType="PolygonGeometry" overrunDistanceUnit="MM" offsetType="0" maxCurvedCharAngleOut="-25" polygonPlacementFlags="2" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistance="0" xOffset="0" geometryGeneratorEnabled="0" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistance="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" maxCurvedCharAngleIn="25" quadOffset="4" fitInPolygonOnly="0" placement="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" distUnits="MM" centroidInside="1" geometryGenerator="" repeatDistanceUnits="MM" priority="10" centroidWhole="0" geometryGeneratorType="PointGeometry" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" yOffset="0" offsetUnits="MM" dist="0"/>
      <rendering fontLimitPixelSize="0" displayAll="0" scaleMax="0" limitNumLabels="0" mergeLines="0" obstacleType="1" drawLabels="1" maxNumLabels="2000" scaleMin="0" upsidedownLabels="0" obstacle="0" fontMaxPixelSize="10000" minFeatureSize="1" zIndex="0" fontMinPixelSize="3" labelPerPart="0" scaleVisibility="0" obstacleFactor="2"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" value="" type="QString"/>
          <Option name="properties"/>
          <Option name="type" value="collection" type="QString"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option name="anchorPoint" value="pole_of_inaccessibility" type="QString"/>
          <Option name="ddProperties" type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
          <Option name="drawToAllParts" value="false" type="bool"/>
          <Option name="enabled" value="0" type="QString"/>
          <Option name="labelAnchorPoint" value="point_on_exterior" type="QString"/>
          <Option name="lineSymbol" value="&lt;symbol name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; alpha=&quot;1&quot; type=&quot;line&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; value=&quot;&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; value=&quot;collection&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" type="QString"/>
          <Option name="minLength" value="0" type="double"/>
          <Option name="minLengthMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
          <Option name="minLengthUnit" value="MM" type="QString"/>
          <Option name="offsetFromAnchor" value="0" type="double"/>
          <Option name="offsetFromAnchorMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
          <Option name="offsetFromAnchorUnit" value="MM" type="QString"/>
          <Option name="offsetFromLabel" value="0" type="double"/>
          <Option name="offsetFromLabelMapUnitScale" value="3x:0,0,0,0,0,0" type="QString"/>
          <Option name="offsetFromLabelUnit" value="MM" type="QString"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties>
    <property value="VM_STAT_ID" key="dualview/previewExpressions"/>
    <property value="transparency" key="embeddedWidgets/0/id"/>
    <property value="1" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory direction="1" spacing="0" backgroundColor="#ffffff" height="15" barWidth="5" lineSizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" backgroundAlpha="255" rotationOffset="270" enabled="0" penWidth="0" maxScaleDenominator="1e+08" spacingUnitScale="3x:0,0,0,0,0,0" showAxis="0" minimumSize="0" sizeType="MM" scaleBasedVisibility="0" opacity="1" spacingUnit="MM" width="15" diagramOrientation="Up" minScaleDenominator="0" labelPlacementMethod="XHeight" penColor="#000000" penAlpha="255" scaleDependency="Area" sizeScale="3x:0,0,0,0,0,0">
      <fontProperties style="" description="Ubuntu,11,-1,5,50,0,0,0,0,0"/>
      <attribute label="" color="#000000" field=""/>
      <axisSymbol>
        <symbol name="" clip_to_extent="1" alpha="1" type="line" force_rhr="0">
          <layer class="SimpleLine" enabled="1" locked="0" pass="0">
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="18" obstacle="0" priority="0" dist="0" zIndex="0" placement="1" showAll="1">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option name="allowedGapsBuffer" value="0" type="double"/>
        <Option name="allowedGapsEnabled" value="false" type="bool"/>
        <Option name="allowedGapsLayer" value="" type="QString"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="RE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="RE1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="RE2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="RE3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="RE4">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="RE5">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="PERCENT">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="PC1">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="PC2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="PC3">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="PC4">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="PC5">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="RE_LABEL">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="false" type="bool"/>
            <Option name="UseHtml" value="false" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="PC_LABEL">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" value="false" type="bool"/>
            <Option name="UseHtml" value="false" type="bool"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LANDZONE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="BD_STATUS">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="BD_SYMBOL">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="VM_CLASS">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="VM_SYMBOL">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="VM_POLY">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="VERSION">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="L">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="V">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="BVG1M">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="BVG1M_PC">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DBVG1M">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DBVG2M">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DBVG5M">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="S20AH">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="S20AI">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="S20AM">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="SOURCE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="VM_STATUS">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="VM_STAT_ID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="SCALE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="OBJECTID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="MAP_NO">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="layer">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="path">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" index="0" field="fid"/>
    <alias name="" index="1" field="RE"/>
    <alias name="" index="2" field="RE1"/>
    <alias name="" index="3" field="RE2"/>
    <alias name="" index="4" field="RE3"/>
    <alias name="" index="5" field="RE4"/>
    <alias name="" index="6" field="RE5"/>
    <alias name="" index="7" field="PERCENT"/>
    <alias name="" index="8" field="PC1"/>
    <alias name="" index="9" field="PC2"/>
    <alias name="" index="10" field="PC3"/>
    <alias name="" index="11" field="PC4"/>
    <alias name="" index="12" field="PC5"/>
    <alias name="" index="13" field="RE_LABEL"/>
    <alias name="" index="14" field="PC_LABEL"/>
    <alias name="" index="15" field="LANDZONE"/>
    <alias name="" index="16" field="BD_STATUS"/>
    <alias name="" index="17" field="BD_SYMBOL"/>
    <alias name="" index="18" field="VM_CLASS"/>
    <alias name="" index="19" field="VM_SYMBOL"/>
    <alias name="" index="20" field="VM_POLY"/>
    <alias name="" index="21" field="VERSION"/>
    <alias name="" index="22" field="L"/>
    <alias name="" index="23" field="V"/>
    <alias name="" index="24" field="BVG1M"/>
    <alias name="" index="25" field="BVG1M_PC"/>
    <alias name="" index="26" field="DBVG1M"/>
    <alias name="" index="27" field="DBVG2M"/>
    <alias name="" index="28" field="DBVG5M"/>
    <alias name="" index="29" field="S20AH"/>
    <alias name="" index="30" field="S20AI"/>
    <alias name="" index="31" field="S20AM"/>
    <alias name="" index="32" field="SOURCE"/>
    <alias name="" index="33" field="VM_STATUS"/>
    <alias name="" index="34" field="VM_STAT_ID"/>
    <alias name="" index="35" field="SCALE"/>
    <alias name="" index="36" field="OBJECTID"/>
    <alias name="" index="37" field="MAP_NO"/>
    <alias name="" index="38" field="layer"/>
    <alias name="" index="39" field="path"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="fid"/>
    <default expression="" applyOnUpdate="0" field="RE"/>
    <default expression="" applyOnUpdate="0" field="RE1"/>
    <default expression="" applyOnUpdate="0" field="RE2"/>
    <default expression="" applyOnUpdate="0" field="RE3"/>
    <default expression="" applyOnUpdate="0" field="RE4"/>
    <default expression="" applyOnUpdate="0" field="RE5"/>
    <default expression="" applyOnUpdate="0" field="PERCENT"/>
    <default expression="" applyOnUpdate="0" field="PC1"/>
    <default expression="" applyOnUpdate="0" field="PC2"/>
    <default expression="" applyOnUpdate="0" field="PC3"/>
    <default expression="" applyOnUpdate="0" field="PC4"/>
    <default expression="" applyOnUpdate="0" field="PC5"/>
    <default expression="" applyOnUpdate="0" field="RE_LABEL"/>
    <default expression="" applyOnUpdate="0" field="PC_LABEL"/>
    <default expression="" applyOnUpdate="0" field="LANDZONE"/>
    <default expression="" applyOnUpdate="0" field="BD_STATUS"/>
    <default expression="" applyOnUpdate="0" field="BD_SYMBOL"/>
    <default expression="" applyOnUpdate="0" field="VM_CLASS"/>
    <default expression="" applyOnUpdate="0" field="VM_SYMBOL"/>
    <default expression="" applyOnUpdate="0" field="VM_POLY"/>
    <default expression="" applyOnUpdate="0" field="VERSION"/>
    <default expression="" applyOnUpdate="0" field="L"/>
    <default expression="" applyOnUpdate="0" field="V"/>
    <default expression="" applyOnUpdate="0" field="BVG1M"/>
    <default expression="" applyOnUpdate="0" field="BVG1M_PC"/>
    <default expression="" applyOnUpdate="0" field="DBVG1M"/>
    <default expression="" applyOnUpdate="0" field="DBVG2M"/>
    <default expression="" applyOnUpdate="0" field="DBVG5M"/>
    <default expression="" applyOnUpdate="0" field="S20AH"/>
    <default expression="" applyOnUpdate="0" field="S20AI"/>
    <default expression="" applyOnUpdate="0" field="S20AM"/>
    <default expression="" applyOnUpdate="0" field="SOURCE"/>
    <default expression="" applyOnUpdate="0" field="VM_STATUS"/>
    <default expression="" applyOnUpdate="0" field="VM_STAT_ID"/>
    <default expression="" applyOnUpdate="0" field="SCALE"/>
    <default expression="" applyOnUpdate="0" field="OBJECTID"/>
    <default expression="" applyOnUpdate="0" field="MAP_NO"/>
    <default expression="" applyOnUpdate="0" field="layer"/>
    <default expression="" applyOnUpdate="0" field="path"/>
  </defaults>
  <constraints>
    <constraint constraints="3" unique_strength="1" notnull_strength="1" exp_strength="0" field="fid"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="RE"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="RE1"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="RE2"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="RE3"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="RE4"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="RE5"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="PERCENT"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="PC1"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="PC2"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="PC3"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="PC4"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="PC5"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="RE_LABEL"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="PC_LABEL"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="LANDZONE"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="BD_STATUS"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="BD_SYMBOL"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="VM_CLASS"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="VM_SYMBOL"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="VM_POLY"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="VERSION"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="L"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="V"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="BVG1M"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="BVG1M_PC"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="DBVG1M"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="DBVG2M"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="DBVG5M"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="S20AH"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="S20AI"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="S20AM"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="SOURCE"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="VM_STATUS"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="VM_STAT_ID"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="SCALE"/>
    <constraint constraints="3" unique_strength="1" notnull_strength="1" exp_strength="0" field="OBJECTID"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="MAP_NO"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="layer"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" exp_strength="0" field="path"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="fid"/>
    <constraint exp="" desc="" field="RE"/>
    <constraint exp="" desc="" field="RE1"/>
    <constraint exp="" desc="" field="RE2"/>
    <constraint exp="" desc="" field="RE3"/>
    <constraint exp="" desc="" field="RE4"/>
    <constraint exp="" desc="" field="RE5"/>
    <constraint exp="" desc="" field="PERCENT"/>
    <constraint exp="" desc="" field="PC1"/>
    <constraint exp="" desc="" field="PC2"/>
    <constraint exp="" desc="" field="PC3"/>
    <constraint exp="" desc="" field="PC4"/>
    <constraint exp="" desc="" field="PC5"/>
    <constraint exp="" desc="" field="RE_LABEL"/>
    <constraint exp="" desc="" field="PC_LABEL"/>
    <constraint exp="" desc="" field="LANDZONE"/>
    <constraint exp="" desc="" field="BD_STATUS"/>
    <constraint exp="" desc="" field="BD_SYMBOL"/>
    <constraint exp="" desc="" field="VM_CLASS"/>
    <constraint exp="" desc="" field="VM_SYMBOL"/>
    <constraint exp="" desc="" field="VM_POLY"/>
    <constraint exp="" desc="" field="VERSION"/>
    <constraint exp="" desc="" field="L"/>
    <constraint exp="" desc="" field="V"/>
    <constraint exp="" desc="" field="BVG1M"/>
    <constraint exp="" desc="" field="BVG1M_PC"/>
    <constraint exp="" desc="" field="DBVG1M"/>
    <constraint exp="" desc="" field="DBVG2M"/>
    <constraint exp="" desc="" field="DBVG5M"/>
    <constraint exp="" desc="" field="S20AH"/>
    <constraint exp="" desc="" field="S20AI"/>
    <constraint exp="" desc="" field="S20AM"/>
    <constraint exp="" desc="" field="SOURCE"/>
    <constraint exp="" desc="" field="VM_STATUS"/>
    <constraint exp="" desc="" field="VM_STAT_ID"/>
    <constraint exp="" desc="" field="SCALE"/>
    <constraint exp="" desc="" field="OBJECTID"/>
    <constraint exp="" desc="" field="MAP_NO"/>
    <constraint exp="" desc="" field="layer"/>
    <constraint exp="" desc="" field="path"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
    <actionsetting notificationMessage="" name="RE description" id="{0ded12ab-08d6-4b3b-abd2-58d2af322037}" isEnabledOnlyWhenEditable="0" shortTitle="" icon="" action="#############################################################################################################&#xa;#                       QGIS Action script for extracting info from                                         #&#xa;#                           https://www.data.qld.gov.au/dataset/                                            #&#xa;#   Data is provided under Creative Commons Attribution 4.0 by the Queensland Government                    #&#xa;#                                                                                                           #&#xa;#                                               By Otto Pattemore                                           #&#xa;#                                                                                                           #&#xa;#############################################################################################################&#xa;import processing&#xa;import re&#xa;import json&#xa;from PyQt5.QtWidgets import *&#xa;from PyQt5.QtGui import *&#xa;class TableMessageBox(QMessageBox):&#xa;    def __init__(self,title, fields,records):&#xa;        QMessageBox.__init__(self)&#xa;        self.setSizeGripEnabled (True)&#xa;        self.records = records&#xa;        self.fields = fields&#xa;        self.setWindowTitle (title)&#xa;&#xa;        #Create QPushButton in QMessageBox        &#xa;        self.addButton (QPushButton('OK'), QMessageBox.YesRole)&#xa;        #Add TableWidget to QMessageBox           &#xa;        self.addTableWidget (self) &#xa;&#xa;        #Return values while clicking QPushButton        &#xa;        currentClick    = self.exec_() &#xa;&#xa;    #Create TableWidget &#xa;    def addTableWidget (self, parentItem):&#xa;        self.tableWidget = QTableWidget(parentItem)&#xa;        self.tableWidget.setGeometry (QtCore.QRect(0, 0, 925, 500))&#xa;        self.tableWidget.setObjectName ('tableWidget')&#xa;        print(len(self.records))&#xa;        self.tableWidget.setColumnCount(len(self.fields))&#xa;        self.tableWidget.setRowCount(len(self.records[&quot;RE&quot;])+1)&#xa;        for row in range(0,len(self.fields)):&#xa;                table_item = QTableWidgetItem(self.fields[row])&#xa;                font = QFont()&#xa;                font.setBold(True)&#xa;                table_item.setFont(font)&#xa;                self.tableWidget.setItem (0,row,table_item)&#xa;                table_item.setBackground(QColor(&quot;green&quot;))&#xa;                for column in range(0,len(self.records[self.fields[row]])):&#xa;                    self.tableWidget.setItem (column+1,row,QTableWidgetItem(self.records[self.fields[row]][column]))&#xa;        #font = QFont()&#xa;        #font.setBold(True)&#xa;        #self.tableWidget.setHeaderFont(font)&#xa;        self.tableWidget.setWordWrap(True)&#xa;        self.tableWidget.setColumnWidth(1,400)&#xa;        self.tableWidget.setColumnWidth(2,150)&#xa;        self.tableWidget.resizeRowsToContents()&#xa;    #Allow resizing of QMessageBox&#xa;    def event(self, e):&#xa;        result = QMessageBox.event(self, e)&#xa;        self.setMinimumWidth(1025)&#xa;        self.setMaximumWidth(16777215)&#xa;        self.setMinimumHeight(400)&#xa;        self.setMaximumHeight(16777215)        &#xa;        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)&#xa;&#xa;        return result&#xa;def GetJSON(URL):&#xa;    #This method of server access avoids firewall problems&#xa;    params = {&#xa;        'URL' : URL,&#xa;        'OUTPUT' : &quot;TEMPORARY_OUTPUT&quot;&#xa;    }&#xa;    tempLayer = processing.run('native:filedownloader',params)[&quot;OUTPUT&quot;]&#xa;    file = open(tempLayer)&#xa;    return_string = file.read()&#xa;    file.close()&#xa;    return return_string&#xa;# Get REs and remove alphabetic characters if they are present&#xa;RE1 = str(&quot;[%RE1%]&quot;)&#xa;RE1 = re.sub(&quot;[^0-9.-]+&quot;,'',RE1)&#xa;RE2 = str(&quot;[%RE2%]&quot;)&#xa;RE2 = re.sub(&quot;[^0-9.-]+&quot;,'',RE2)&#xa;RE3 = str(&quot;[%RE3%]&quot;)&#xa;RE3 = re.sub(&quot;[^0-9.-]+&quot;,'',RE3)&#xa;RE4 = str(&quot;[%RE4%]&quot;)&#xa;RE4 = re.sub(&quot;[^0-9.-]+&quot;,'',RE4)&#xa;RE5 = str(&quot;[%RE5%]&quot;)&#xa;RE5 = re.sub(&quot;[^0-9.-]+&quot;,'',RE5)&#xa;res = [RE1,RE2,RE3,RE4,RE5]&#xa;short_descriptions = []&#xa;vma_classes = []&#xa;structure = []&#xa;for i in res:&#xa;    url = 'https://www.data.qld.gov.au/api/3/action/datastore_search?resource_id=adb569fd-c660-40ad-a4ed-2b9c3eda7023&amp;filters={&quot;re_id&quot;:&quot;'+str(i)+'&quot;}'&#xa;    json_data = json.loads(GetJSON(url))&#xa;    for j in json_data['result']['records']:&#xa;        short_descriptions.append(j[&quot;Short Description Regulation&quot;])&#xa;        vma_classes.append(j[&quot;vma_class&quot;])&#xa;        structure.append(j[&quot;Structure category&quot;])&#xa;&#xa;msg = TableMessageBox('Regional Ecosystem(s)',[&quot;RE&quot;,&quot;Short description&quot;,&quot;VMA class&quot;,&quot;Structure&quot;],{&#xa;    &quot;RE&quot;:res,&#xa;    &quot;Short description&quot;:short_descriptions,&#xa;    &quot;VMA class&quot;:vma_classes,&#xa;    &quot;Structure&quot;:structure&#xa;})" type="1" capture="0">
      <actionScope id="Canvas"/>
      <actionScope id="Feature"/>
      <actionScope id="Field"/>
      <actionScope id="Layer"/>
    </actionsetting>
    <actionsetting notificationMessage="" name="Create Google Earth KML file" id="{7c46e589-b1c0-4b40-be66-db8b735ceba3}" isEnabledOnlyWhenEditable="0" shortTitle="" icon="" action="#############################################################################################################&#xa;#                       QGIS Action script for creating KML with styling                                    #&#xa;#                                                                                                           #&#xa;#   Data is provided under Creative Commons Attribution 4.0 by the Queensland Government                    #&#xa;#                                                                                                           #&#xa;#                                written by Gary and Otto Pattemore                                         #&#xa;#                                released under Creative Commons Attribution 4.0                            #&#xa;#############################################################################################################&#xa;#&#xa;from qgis.core import QgsExpression&#xa;from qgis.PyQt.QtCore import *&#xa;from PyQt5.QtWidgets import *&#xa;import processing&#xa;from qgis.utils import iface&#xa;from os import path&#xa;#&#xa;dir = os.path.expanduser('~')&#xa;# setup progress bar&#xa;progressMessageBar = iface.messageBar().createMessage(&quot;Styling and building Google KML file...&quot;)&#xa;progress = QProgressBar()&#xa;progress.setMaximum(100)&#xa;progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)&#xa;progressMessageBar.layout().addWidget(progress)&#xa;iface.messageBar().pushWidget(progressMessageBar, Qgis.Info)&#xa;#&#xa;layer = iface.activeLayer()&#xa;layer.selectAll()&#xa;progress.setValue(1)&#xa;progress.setFormat(&quot;Styling KML...&quot;)&#xa;clone_layer = processing.run(&quot;native:saveselectedfeatures&quot;, {'INPUT': layer, 'OUTPUT': 'memory:'})['OUTPUT']&#xa;layer.removeSelection()&#xa;progress.setValue(2)&#xa;caps = clone_layer.dataProvider().capabilities()&#xa;if caps &amp; QgsVectorDataProvider.AddAttributes:&#xa;    res = clone_layer.dataProvider().addAttributes(&#xa;        [QgsField(&quot;K_Name&quot;, QVariant.String),&#xa;        QgsField(&quot;K_Status&quot;, QVariant.String),&#xa;        QgsField(&quot;OGR_STYLE&quot;, QVariant.String)])&#xa;    clone_layer.updateFields()&#xa;    progress.setValue(10)&#xa;    #&#xa;    clone_layer.startEditing()&#xa;    totalf = clone_layer.featureCount()&#xa;    for i,feat in enumerate(clone_layer.getFeatures()):&#xa;        expr1 = str(feat['RE_LABEL']+' ('+feat['PC_LABEL']+')')&#xa;        expr4 = 'Supporting Map'+' '+expr1&#xa;        if feat['S20AH'] == None:&#xa;            expr2 = str(feat['VM_STATUS'])&#xa;        else:&#xa;            expr2 = str(feat['VM_STATUS']+feat['S20AH'])&#xa;        if expr2 =='rem_end ':&#xa;            expr3 = 'BRUSH(fc:#ff36ff);PEN(c:#000000);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 =='rem_oc ':&#xa;            expr3 = 'BRUSH(fc:#ff650f);PEN(c:#000000);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 =='rem_leastc ':&#xa;            expr3 = 'BRUSH(fc:#7dffb1);PEN(c:#000000);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 =='rem_endVMA S20AH area':&#xa;            expr3 = 'BRUSH(fc:#ff36ff);PEN(c:#ffff73);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 =='rem_ocVMA S20AH area':&#xa;            expr3 = 'BRUSH(fc:#ff650f);PEN(c:#ffff73);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 =='rem_leastcVMA S20AH area':&#xa;            expr3 = 'BRUSH(fc:#7dffb1);PEN(c:#ffff73);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 =='hvr_end ':&#xa;            expr3 = 'BRUSH(fc:#ffa8ff);PEN(c:#000000);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 =='hvr_oc ':&#xa;            expr3 = 'BRUSH(fc:#ffd091);PEN(c:#000000);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 =='hvr_leastc ':&#xa;            expr3 = 'BRUSH(fc:#d7ffb1);PEN(c:#000000);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 == 'non_remnant ':&#xa;            expr3 = 'BRUSH(fc:#feffff);PEN(c:#000000);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        elif expr2 == 'water ':&#xa;            expr3 = 'BRUSH(fc:#e1ffff);PEN(c:#000000);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        else:&#xa;            expr3 = 'BRUSH(fc:#ff0000);PEN(c:#000000);LABEL(f:&quot;Arial, Helvetica&quot;, s:12pt, t:&quot;'+expr4+'&quot;)'&#xa;        #print(expr1, ' ' , expr2, ' ' , expr3, ' ')&#xa;        feat['K_Name'] = expr1&#xa;        feat['K_Status'] = expr2&#xa;        feat['OGR_STYLE'] = expr3&#xa;        clone_layer.updateFeature(feat)&#xa;        progress.setValue(int(i/totalf*40)+10)&#xa;    clone_layer.commitChanges()&#xa;    #&#xa;#&#xa;progress.setValue(50)&#xa;progress.setFormat(&quot;Building Google KML file...  (may take a while)&quot;)&#xa;preferedName = str(&quot;[% concat(@layer_name ,'_', now()) %]&quot;)[:-10]&#xa;preferedName = dir+'/'+preferedName+'.kml'&#xa;fname, _ = QFileDialog.getSaveFileName(None, &quot;Save Google KML file&quot;, preferedName, &quot;Google KML (*.kml)&quot;)&#xa;project = QgsProject.instance()&#xa;canvas = iface.mapCanvas()&#xa;canvasExtent = canvas.extent()&#xa;xmin = str(canvasExtent.xMinimum())&#xa;ymin = str(canvasExtent.yMinimum())&#xa;xmax = str(canvasExtent.xMaximum())&#xa;ymax = str(canvasExtent.yMaximum())&#xa;ExtentString = xmin+&quot; &quot;+ymin+&quot; &quot;+xmax+&quot; &quot;+ymax&#xa;options = '-clipsrc '+ExtentString&#xa;progress.setValue(60)&#xa;kml_layer = processing.run(&quot;gdal:convertformat&quot;, {'INPUT': clone_layer, 'OPTIONS': options, 'OUTPUT': str(fname)})['OUTPUT']&#xa;progress.setValue(100)&#xa;iface.messageBar().clearWidgets()&#xa;QMessageBox.about(None, &quot;Create Google KML&quot;, &quot;Google KML file saved as: &quot;+fname)&#xa;#&#xa;#&#xa;&#xa;" type="1" capture="0">
      <actionScope id="Canvas"/>
      <actionScope id="Feature"/>
      <actionScope id="Field"/>
      <actionScope id="Layer"/>
    </actionsetting>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column name="RE" hidden="0" width="-1" type="field"/>
      <column name="RE1" hidden="0" width="-1" type="field"/>
      <column name="RE2" hidden="0" width="-1" type="field"/>
      <column name="RE3" hidden="0" width="-1" type="field"/>
      <column name="RE4" hidden="0" width="-1" type="field"/>
      <column name="RE5" hidden="0" width="-1" type="field"/>
      <column name="PERCENT" hidden="0" width="-1" type="field"/>
      <column name="PC1" hidden="0" width="-1" type="field"/>
      <column name="PC2" hidden="0" width="-1" type="field"/>
      <column name="PC3" hidden="0" width="-1" type="field"/>
      <column name="PC4" hidden="0" width="-1" type="field"/>
      <column name="PC5" hidden="0" width="-1" type="field"/>
      <column name="RE_LABEL" hidden="0" width="-1" type="field"/>
      <column name="PC_LABEL" hidden="0" width="-1" type="field"/>
      <column name="LANDZONE" hidden="0" width="-1" type="field"/>
      <column name="BD_STATUS" hidden="0" width="-1" type="field"/>
      <column name="BD_SYMBOL" hidden="0" width="-1" type="field"/>
      <column name="VM_CLASS" hidden="0" width="-1" type="field"/>
      <column name="VM_SYMBOL" hidden="0" width="-1" type="field"/>
      <column name="VM_POLY" hidden="0" width="-1" type="field"/>
      <column name="VERSION" hidden="0" width="-1" type="field"/>
      <column name="L" hidden="0" width="-1" type="field"/>
      <column name="V" hidden="0" width="-1" type="field"/>
      <column name="BVG1M" hidden="0" width="-1" type="field"/>
      <column name="BVG1M_PC" hidden="0" width="-1" type="field"/>
      <column name="DBVG1M" hidden="0" width="-1" type="field"/>
      <column name="DBVG2M" hidden="0" width="-1" type="field"/>
      <column name="DBVG5M" hidden="0" width="-1" type="field"/>
      <column name="S20AH" hidden="0" width="262" type="field"/>
      <column name="S20AI" hidden="0" width="-1" type="field"/>
      <column name="S20AM" hidden="0" width="-1" type="field"/>
      <column name="SOURCE" hidden="0" width="-1" type="field"/>
      <column name="VM_STATUS" hidden="0" width="-1" type="field"/>
      <column name="VM_STAT_ID" hidden="0" width="-1" type="field"/>
      <column name="SCALE" hidden="0" width="-1" type="field"/>
      <column name="OBJECTID" hidden="0" width="-1" type="field"/>
      <column name="MAP_NO" hidden="0" width="-1" type="field"/>
      <column hidden="1" width="-1" type="actions"/>
      <column name="layer" hidden="0" width="-1" type="field"/>
      <column name="path" hidden="0" width="-1" type="field"/>
      <column name="fid" hidden="0" width="-1" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="BD_STATUS" editable="1"/>
    <field name="BD_SYMBOL" editable="1"/>
    <field name="BVG1M" editable="1"/>
    <field name="BVG1M_PC" editable="1"/>
    <field name="DBVG1M" editable="1"/>
    <field name="DBVG2M" editable="1"/>
    <field name="DBVG5M" editable="1"/>
    <field name="L" editable="1"/>
    <field name="LANDZONE" editable="1"/>
    <field name="MAP_NO" editable="1"/>
    <field name="OBJECTID" editable="1"/>
    <field name="PC1" editable="1"/>
    <field name="PC2" editable="1"/>
    <field name="PC3" editable="1"/>
    <field name="PC4" editable="1"/>
    <field name="PC5" editable="1"/>
    <field name="PC_LABEL" editable="1"/>
    <field name="PERCENT" editable="1"/>
    <field name="RE" editable="1"/>
    <field name="RE1" editable="1"/>
    <field name="RE2" editable="1"/>
    <field name="RE3" editable="1"/>
    <field name="RE4" editable="1"/>
    <field name="RE5" editable="1"/>
    <field name="RE_LABEL" editable="1"/>
    <field name="S20AH" editable="1"/>
    <field name="S20AI" editable="1"/>
    <field name="S20AM" editable="1"/>
    <field name="SCALE" editable="1"/>
    <field name="SOURCE" editable="1"/>
    <field name="V" editable="1"/>
    <field name="VERSION" editable="1"/>
    <field name="VM_CLASS" editable="1"/>
    <field name="VM_POLY" editable="1"/>
    <field name="VM_STATUS" editable="1"/>
    <field name="VM_STAT_ID" editable="1"/>
    <field name="VM_SYMBOL" editable="1"/>
    <field name="fid" editable="1"/>
    <field name="layer" editable="1"/>
    <field name="path" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="BD_STATUS" labelOnTop="0"/>
    <field name="BD_SYMBOL" labelOnTop="0"/>
    <field name="BVG1M" labelOnTop="0"/>
    <field name="BVG1M_PC" labelOnTop="0"/>
    <field name="DBVG1M" labelOnTop="0"/>
    <field name="DBVG2M" labelOnTop="0"/>
    <field name="DBVG5M" labelOnTop="0"/>
    <field name="L" labelOnTop="0"/>
    <field name="LANDZONE" labelOnTop="0"/>
    <field name="MAP_NO" labelOnTop="0"/>
    <field name="OBJECTID" labelOnTop="0"/>
    <field name="PC1" labelOnTop="0"/>
    <field name="PC2" labelOnTop="0"/>
    <field name="PC3" labelOnTop="0"/>
    <field name="PC4" labelOnTop="0"/>
    <field name="PC5" labelOnTop="0"/>
    <field name="PC_LABEL" labelOnTop="0"/>
    <field name="PERCENT" labelOnTop="0"/>
    <field name="RE" labelOnTop="0"/>
    <field name="RE1" labelOnTop="0"/>
    <field name="RE2" labelOnTop="0"/>
    <field name="RE3" labelOnTop="0"/>
    <field name="RE4" labelOnTop="0"/>
    <field name="RE5" labelOnTop="0"/>
    <field name="RE_LABEL" labelOnTop="0"/>
    <field name="S20AH" labelOnTop="0"/>
    <field name="S20AI" labelOnTop="0"/>
    <field name="S20AM" labelOnTop="0"/>
    <field name="SCALE" labelOnTop="0"/>
    <field name="SOURCE" labelOnTop="0"/>
    <field name="V" labelOnTop="0"/>
    <field name="VERSION" labelOnTop="0"/>
    <field name="VM_CLASS" labelOnTop="0"/>
    <field name="VM_POLY" labelOnTop="0"/>
    <field name="VM_STATUS" labelOnTop="0"/>
    <field name="VM_STAT_ID" labelOnTop="0"/>
    <field name="VM_SYMBOL" labelOnTop="0"/>
    <field name="fid" labelOnTop="0"/>
    <field name="layer" labelOnTop="0"/>
    <field name="path" labelOnTop="0"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"VM_STAT_ID"</previewExpression>
  <mapTip>&lt;iframe src="/default.asp" width="300" height="1">
&lt;/iframe>	
&lt;div style = "background-color:LightCoral;">
&lt;h3> [% concat( 'Area = ', round($area,2), ' ' , 
	if (@project_area_units = 'hectares', ' ha', 
		if(@project_area_units = 'square meters', ' sq. m.', @project_area_units))) %] &lt;br>&lt;/h3>
&lt;a [% concat( 'href="https://apps.des.qld.gov.au/regional-ecosystems/details/?re=',  
	"RE1",'"' ) %] style=color:white>[% "RE1" %]&lt;/a>
&lt;a [% concat( 'href="https://apps.des.qld.gov.au/regional-ecosystems/details/?re=',  
	"RE2",'"' ) %] style=color:white>[% "RE2" %]&lt;/a>
&lt;a [% concat( 'href="https://apps.des.qld.gov.au/regional-ecosystems/details/?re=',  
	"RE3",'"' ) %] style=color:white>[% "RE3" %]&lt;/a>
&lt;a [% concat( 'href="https://apps.des.qld.gov.au/regional-ecosystems/details/?re=',  
	"RE4",'"' ) %] style=color:white>[% "RE4" %]&lt;/a>
&lt;a [% concat( 'href="https://apps.des.qld.gov.au/regional-ecosystems/details/?re=',  
	"RE5",'"' ) %] style=color:white>[% "RE5" %]&lt;/a>
&lt;/div>
</mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
