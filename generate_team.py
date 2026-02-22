def generate_html():
    data = """Santiago Vargas Domínguez,Investigador,Universidad Nacional de Colombia,svargasd@unal.edu.co,https://www.researchgate.net/profile/Santiago-Vargas-Dominguez-2
Benjamín Calvo Mozo,Investigador,Universidad Nacional de Colombia,bcalvom@unal.edu.co,https://www.researchgate.net/profile/Benjamin-Calvo-Mozo
Juan Carlos Martínez Oliveros,Investigador,N/A,N/A,https://www.researchgate.net/profile/Juan-Martinez-Oliveros
Domenico Bonaccini Calia,Investigador,N/A,N/A,N/A
Juan Camilo Buitrago Casas,Investigador,N/A,N/A,https://www.researchgate.net/profile/Juan-Camilo-Buitrago-Casas
Juan Camilo Guevara Gómez,Investigador,Universidad de Oslo,j.c.g.gomez@astro.uio.no,N/A
Jose Iván Campos Rozo,Investigador,Universidad de Graz,jose.campos-rozo@edu.uni-graz.at,N/A
Dominik Utz,Investigador,N/A,N/A,https://www.researchgate.net/profile/Dominik-Utz
Javier Sánchez González,Estudiante Maestría,Universidad Nacional de Colombia,jsanchezg@unal.edu.co,https://www.researchgate.net/profile/Javier-Sanchez-Gonzalez
Juan Pablo Herrera Moreno,Estudiante Maestría,Universidad Nacional de Colombia,juapherreramor@unal.edu.co,N/A
Juan Esteban Agudelo Ortiz,Estudiante Maestría,Universidad Nacional de Colombia,N/A,N/A
Paula Jessica González Prieto,Estudiante Maestría,Universidad Nacional de Colombia,pjgonzalezp@unal.edu.co,N/A
Andrés Felipe Guerrero Guio,Estudiante Maestría,Universidad Nacional de Colombia,afguerrerogu@unal.edu.co,N/A
Daniel Alberto Rodríguez Torres,Estudiante Pregrado,Universidad Nacional de Colombia,darodriguezto@unal.edu.co,N/A
Samuel Felipe Noreña Téllez,Estudiante Pregrado,Universidad Nacional de Colombia,sanorenat@unal.edu.co,https://www.researchgate.net/profile/Samuel-Norena-Tellez
Laura Viviana Alfonso Díaz,Estudiante Pregrado,Universidad Nacional de Colombia,lalfonsod@unal.edu.co,N/A
Danna Vanessa Ortiz Carrillo,Estudiante Pregrado,Universidad Nacional de Colombia,daortizca@unal.edu.co,N/A
Laura Vanessa Olaya Zuleta,Estudiante Pregrado,Universidad Nacional de Colombia,N/A,N/A
Julian Andrés Riveros Pacheco,Estudiante Pregrado,Universidad Nacional de Colombia,jriverosp@unal.edu.co,N/A
Juan Felipe Angel Rubio,Estudiante Pregrado,Universidad Nacional de Colombia,N/A,N/A
Oscar Andres Calvo Rebellon,Estudiante Otras Inst.,Universidad del Quindío,oscara.calvor@uqvirtual.edu.co,N/A
Ana Gabriela Martínez,Estudiante Otras Inst.,N/A,N/A,N/A
Nicoll Valeria Moreno Alzate,Estudiante Otras Inst.,N/A,N/A,N/A
Bárbara Elizabeth Riquelme R,Estudiante Otras Inst.,PUC Chile,bzriquelme@uc.cl,https://www.researchgate.net/profile/Barbara-Riquelme-2
Katalina Londoño Espinosa,Estudiante Otras Inst.,Universidad ECCI,Katalina.londonoe@ecci.edu.co,N/A
Juan Camilo Hernández Clavijo,Estudiante Otras Inst.,N/A,juancamilohdez2005@gmail.com,N/A
Laura Camila Palacino Téllez,Estudiante Otras Inst.,Univ. Pedagógica Nacional,laurapalacino24@gmail.com,N/A
Juan Camilo Buitrago,Egresado,Universidad Nacional de Colombia,N/A,https://www.researchgate.net/profile/Juan-Camilo-Buitrago-Casas
Angel Daniel Martínez,Egresado,Universidad Nacional de Colombia,andmartinezci@unal.edu.co,https://www.researchgate.net/profile/Angel_Martinez67
Natalia Granados Hernández,Egresado,Universidad Nacional de Colombia,ngranadosh@unal.edu.co,N/A
Germain Nicolas Morales Suárez,Egresado,Universidad Nacional de Colombia,N/A,N/A
Erika Paola Puentes León,Egresado,Universidad Nacional de Colombia,eppuentesl@unal.edu.co,https://www.researchgate.net/profile/Erika-Puentes-2
Valeria Quintero Ortega,Egresado,Universidad Nacional de Colombia,vquinteroo@unal.edu.co,https://www.researchgate.net/profile/Valeria-Quintero-Ortega
Francisco Javier Ordonez Araujo,Egresado,Universidad Nacional de Colombia,N/A,N/A"""

    colors = {
        'Investigador': '9d4edd',
        'Estudiante Maestría': 'ff7900',
        'Estudiante Pregrado': '00b4d8',
        'Estudiante Otras Inst.': 'fb8500',
        'Egresado': '2a9d8f'
    }

    html = '<div class="team-filter-container">\n'
    html += '    <button class="filter-btn active" data-filter="all">Todos</button>\n'
    html += '    <button class="filter-btn" data-filter="investigador">Investigadores</button>\n'
    html += '    <button class="filter-btn" data-filter="maestria">MSc</button>\n'
    html += '    <button class="filter-btn" data-filter="pregrado">Pregrado</button>\n'
    html += '    <button class="filter-btn" data-filter="otras">Otras Inst.</button>\n'
    html += '    <button class="filter-btn" data-filter="egresado">Egresados</button>\n'
    html += '</div>\n\n<div class="team-grid-full">\n'

    for line in data.strip().split('\n'):
        name, cat, inst, email, rg = line.split(',')
        
        # map cat to filter
        filter_class = ''
        if cat == 'Investigador': filter_class = 'investigador'
        if cat == 'Estudiante Maestría': filter_class = 'maestria'
        if cat == 'Estudiante Pregrado': filter_class = 'pregrado'
        if cat == 'Estudiante Otras Inst.': filter_class = 'otras'
        if cat == 'Egresado': filter_class = 'egresado'
        
        color = colors.get(cat, 'ffffff')
        url_name = name.replace(' ', '+')
        
        html += f'    <div class="team-member-card glassmorphism {filter_class}">\n'
        html += f'        <img src="https://ui-avatars.com/api/?name={url_name}&background={color}&color=fff&size=150" alt="{name}" class="team-avatar-img">\n'
        html += f'        <h4>{name}</h4>\n'
        html += f'        <p class="role">{cat}</p>\n'
        if inst != 'N/A':
            html += f'        <p class="inst">{inst}</p>\n'
        html += '        <div class="member-links">\n'
        if email != 'N/A':
            html += f'            <a href="mailto:{email}" class="member-link" title="Email">✉️</a>\n'
        if rg != 'N/A':
            html += f'            <a href="{rg}" target="_blank" class="member-link" title="ResearchGate">🔬 RG</a>\n'
        html += '        </div>\n'
        html += '    </div>\n'
        
    html += '</div>'
    
    with open('/home/carlmarxt/Documents/gosa_clon/members.html', 'w') as f:
        f.write(html)

generate_html()
