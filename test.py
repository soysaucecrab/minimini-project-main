import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 태양계 행성들의 초기 데이터
# 각 행성의 궤도 반지름 (semi-major axis) (단위: km)
semi_major_axes = {
    'Mercury': 57909050,
    'Venus': 108208000,
    'Earth': 149598262,
    'Mars': 227939100,
    'Jupiter': 778547200,
    'Saturn': 1433449370,
    'Uranus': 2876679082,
    'Neptune': 4503443661
}

# 각 행성의 타원 궤도의 장반경 (단위: km)
# eccentricity = 0이면 원 궤도, 0 < eccentricity < 1이면 타원 궤도
eccentricities = {
    'Mercury': 0.2056,
    'Venus': 0.0068,
    'Earth': 0.0167,
    'Mars': 0.0934,
    'Jupiter': 0.0483,
    'Saturn': 0.056,
    'Uranus': 0.0461,
    'Neptune': 0.0097
}

# 캐플러의 법칙을 이용하여 주기 계산
def get_orbital_period(semi_major_axis):
    G = 6.67430e-11  # 중력 상수 (m^3/kg/s^2)
    M_sun = 1.989e30  # 태양의 질량 (kg)
    a = semi_major_axis * 1000  # semi_major_axis를 m로 변환
    return 2 * np.pi * np.sqrt(a**3 / (G * M_sun)) / (60 * 60 * 24)  # 일 단위로 변환

# 각 행성의 주기 계산
orbital_periods = {planet: get_orbital_period(semi_major_axes[planet]) for planet in semi_major_axes}

# 각 행성의 궤도를 계산하여 그래프에 추가
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for planet in semi_major_axes:
    semi_major_axis = semi_major_axes[planet]
    eccentricity = eccentricities[planet]
    period = orbital_periods[planet]
    
    theta = np.linspace(0, 2*np.pi, 1000)
    r = semi_major_axis * (1 - eccentricity**2) / (1 + eccentricity * np.cos(theta))
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.zeros_like(theta)   # z 값은 semi_major_axis로 설정하여 순차적으로 증가하도록 함
    
    ax.plot(x, y, z, label=planet)

ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
ax.set_title('Solar System Planetary Orbits')
ax.legend()
plt.show()