#!fontforge --lang=py -script

import fontforge
import psMat
import math

# �s�p�m�[�h���c��2�_�Ԃɓ������֐��B
# ���e�����ŏ��p�x�̓f�t�H���g��2��
def ys_trim_spikes(glyph, angle_threshold=2):
    angle_threshold_rad = math.radians(angle_threshold)  # �p�x�����W�A���ɕϊ�
    for contour in glyph.foreground:
        i = 0
        while i < len(contour):
            # �m�[�h�̑O����擾�i���[�v���l�����āj
            current_point = contour[i]
            # �I���N���[�u�|�C���g�݂̂�ΏۂƂ���
            if not current_point.on_curve:
                i += 1
                continue
            # �O��̃I���N���[�u�|�C���g���擾
            prev_index = i - 1
            while not contour[prev_index % len(contour)].on_curve:
                prev_index -= 1
            next_index = i + 1
            while not contour[next_index % len(contour)].on_curve:
                next_index += 1
            prev_point = contour[prev_index % len(contour)]
            next_point = contour[next_index % len(contour)]
            
            # ���W���擾
            prev_coords = (prev_point.x, prev_point.y)
            current_coords = (current_point.x, current_point.y)
            next_coords = (next_point.x, next_point.y)
            
            # �x�N�g�����v�Z
            vector1 = (prev_coords[0] - current_coords[0], prev_coords[1] - current_coords[1])
            vector2 = (next_coords[0] - current_coords[0], next_coords[1] - current_coords[1])
            
            # �x�N�g���̑傫���Ɠ��ς��v�Z
            mag1 = math.hypot(*vector1)
            mag2 = math.hypot(*vector2)
            dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
            
            # �p�x���v�Z
            if mag1 > 0 and mag2 > 0:  # �[�����Z���
                cos_angle = dot_product / (mag1 * mag2)
                cos_angle = max(-1, min(1, cos_angle))  # ���������_�덷�̕␳
                angle = math.acos(cos_angle)
                # �p�x��臒l�����Ȃ�C��
                if angle < angle_threshold_rad:
                    # ���ԓ_���v�Z���Ĉړ�
                    midpoint = ((prev_coords[0] + next_coords[0]) / 2,
                                (prev_coords[1] + next_coords[1]) / 2)
                    current_point.x, current_point.y = midpoint
            i += 1

if __name__ == "__main__":
    ys_trim_spikes(glyph, angle_threshold=2)
